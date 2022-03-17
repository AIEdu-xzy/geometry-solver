from typing import Union

from geometry_solver.indexer.base_indexer import BaseIndexer
from geometry_solver.graph.deduction_graph import DeductionGraph
from geometry_solver.condition import RelationshipBased
from geometry_solver.condition.condition import Condition
from geometry_solver.entity import Entity
from geometry_solver.relationship import Relationship
import geometry_solver.entity
import geometry_solver.relationship


class TypeIndexer(BaseIndexer):
    
    def __init__(self,
            entity: Entity, 
            graph: DeductionGraph):
        # In this table, key is entity/relationship type, and value 
        # is a list of entities/relationships of this type.
        keys = []
        e_names = geometry_solver.entity.__all__
        r_names = geometry_solver.relationship.__all__
        for name in e_names:
            if name == 'Entity':
                continue
            keys.append(getattr(geometry_solver.entity, name))
        for name in r_names:
            if name == 'Relationship':
                continue
            keys.append(getattr(geometry_solver.relationship, name))
        self.table = {}
        for key in keys:
            self.table[key] = []
        self.build_index(entity, graph)
    
    def build_index(self,
            entity: Entity, 
            graph: DeductionGraph):
        for e in entity.children:
            self.table[type(e)].append(e)
        for cond in graph.conditions:
            if type(cond) == RelationshipBased:
                r = cond.relationship
                self.table[type(r)].append(cond)

    def update_index(self, new_obj: Union[Condition, Entity]):
        if isinstance(new_obj, Entity):
            self.table[type(e)].append(new_obj)
        elif type(new_obj) == RelationshipBased:
            r = new_obj.relationship
            self.table[type(r)].append(new_obj)

    def index(self, type_):
        """Return a list of entity/relationship condition of this type."""
        return self.table[type_]
    
