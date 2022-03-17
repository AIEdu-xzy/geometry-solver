import torch
import math

import geometry_solver.reinforcement_learning.env_params as env_params
from geometry_solver.problem import Problem
from geometry_solver.entity import Entity
from geometry_solver.condition import RelationshipBased
import geometry_solver.theorem

_theorems = None

def initialize_theorems():
    global _theorems
    if _theorems is None:
        _theorems = geometry_solver.theorem.valid_theorem
        _theorems = [th() for th in _theorems]
    return _theorems


def state_encoding(problem, device, last_step):
    """Extract tensor presentation of environment.

    Return a map encodes diffirent types of component.
    """
    state_map = {}
    state_map['entity'] = _entity_encoding(problem, device)
    state_map['relationship'] = _relationship_encoding(problem, device)
    state_map['target'] = _target_encoding(problem, device)
    state_map['action_mask'] = _action_mask_encoding(problem, device)
    if last_step is not None:
        state_map['action_mask'][last_step] = 0
    return state_map


def _entity_encoding(problem, device):
    entity_type_tensor = torch.zeros(
            env_params.MAX_ENTITIES,
            env_params.ENTITY_TYPE_NUM,
            dtype=torch.float32, device=device)
    entity_attribute_tensor = torch.zeros(
            env_params.MAX_ENTITIES,
            env_params.ENTITY_ATTRIBUTE_NUM,
            dtype=torch.float32, device=device)
    indexer = problem.indexer
    entity_list = list(problem.entity.children)

    for i, e in enumerate(entity_list):
        type_index = env_params.ALL_ENTITY_TYPE.index(type(e))
        entity_type_tensor[i, type_index] = 1
        for j, attr in enumerate(env_params.ENTITY_ATTRIBUTES[type(e)]):
            cond = indexer.index_value_condition(e, attr, create_when_not_found=False)
            if cond is not None:
                entity_attribute_tensor[i, j] = 1

    entity_tensor = torch.cat((entity_type_tensor, entity_attribute_tensor), dim=1)
    return entity_tensor


def _relationship_encoding(problem, device):
    relationship_type_tensor = torch.zeros(
            env_params.MAX_RELATIONSHIPS,
            env_params.RELATIONSHIP_TYPE_NUM,
            dtype=torch.float32, device=device)
    relationship_attribute_tensor = torch.zeros(
            env_params.MAX_RELATIONSHIPS,
            env_params.RELATIONSHIP_ATTRIBUTE_NUM,
            dtype=torch.float32, device=device)
    relationship_link_entity_tensor = torch.zeros(
            env_params.MAX_RELATIONSHIPS,
            env_params.MAX_ENTITIES,
            dtype=torch.float32, device=device)
    indexer = problem.indexer
    entity_list = list(problem.entity.children)

    relationships = [cond.relationship for cond in problem.conditions \
            if type(cond) == RelationshipBased]

    for i, r in enumerate(relationships):
        type_index = env_params.ALL_RELATIONSHIP_TYPE.index(type(r))
        relationship_type_tensor[i, type_index] = 1
        for j, attr in enumerate(env_params.RELATIONSHIP_ATTRIBUTES[type(r)]):
            cond = indexer.index_value_condition(r, attr, create_when_not_found=False)
            if cond is not None:
                relationship_attribute_tensor[i, j] = 1

        for member_str in dir(r):
            member = getattr(r, member_str)
            if isinstance(member, Entity):
                entity_index = entity_list.index(member)
                relationship_link_entity_tensor[i, entity_index] = 1
            elif isinstance(member, list):
                for e in member:
                    if isinstance(e, Entity):
                        entity_index = entity_list.index(e)
                        relationship_link_entity_tensor[i, entity_index] = 1

    relationship_tensor = torch.cat(
            (relationship_type_tensor,
             relationship_attribute_tensor,
             relationship_link_entity_tensor), dim=1)
    return relationship_tensor


def _target_encoding(problem, device):
    target_tensor = torch.zeros(
            env_params.MAX_ENTITIES
            + env_params.ENTITY_ATTRIBUTE_NUM
            + env_params.MAX_RELATIONSHIPS
            + env_params.RELATIONSHIP_ATTRIBUTE_NUM,
            dtype=torch.float32, device=device)
    target = problem.target
    entity_list = list(problem.entity.children)
    relationships = [cond.relationship for cond in problem.conditions \
            if type(cond) == RelationshipBased]

    if target.obj in entity_list:
        obj_index = entity_list.index(target.obj)
        target_tensor[obj_index] = 1
        attr_index = env_params.ENTITY_ATTRIBUTES[type(target.obj)].index(target.attr)
        target_tensor[env_params.MAX_ENTITIES + attr_index] = 1
    else:
        base = env_params.MAX_ENTITIES + env_params.ENTITY_ATTRIBUTE_NUM
        obj_index = relationships.index(target.obj)
        target_tensor[base + obj_index] = 1
        attr_index = env_params.RELATIONSHIP_ATTRIBUTES[type(target.obj)].index(target.attr)
        target_tensor[base + env_params.MAX_RELATIONSHIPS + attr_index] = 1

    return target_tensor


def _action_mask_encoding(problem, device):
    action_mask_tensor = torch.zeros(
            env_params.THEOREM_NUM,
            dtype=torch.uint8,
            device=device)
    theorems = initialize_theorems()
    for i, th in enumerate(theorems):
        if problem.is_valid(th):
            action_mask_tensor[i] = 1
    return action_mask_tensor


def normal_distribution_value(x, mu, std):
    denominator = math.exp(-((x-mu)**2) / (2*(std**2)))
    divisor = math.sqrt(2 * math.pi * (std**2))
    return denominator / divisor


