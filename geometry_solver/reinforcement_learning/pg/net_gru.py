import torch
import torch.nn as nn
import torch.nn.functional as F

import geometry_solver.reinforcement_learning.env_params as env_params


class Net(nn.Module):

    def __init__(self, device):
        super().__init__()
        self.device = device

        self.entity_encoder = nn.Sequential(
            nn.Linear(env_params.ENTITY_TYPE_NUM + env_params.ENTITY_ATTRIBUTE_NUM, 32),
            nn.ReLU(),
            nn.Linear(32, 8),
            nn.ReLU(),
            nn.Linear(8, 1)
        )
        self.relationship_encoder = nn.Sequential(
            nn.Linear(env_params.RELATIONSHIP_TYPE_NUM
                      + env_params.RELATIONSHIP_ATTRIBUTE_NUM
                      + env_params.MAX_ENTITIES, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 8),
            nn.ReLU(),
            nn.Linear(8, 1)
        )

        TARGET_ENCODING_SIZE = 16

        self.target_encoder = nn.Sequential(
            nn.Linear(env_params.MAX_ENTITIES
                    + env_params.ENTITY_ATTRIBUTE_NUM
                    + env_params.MAX_RELATIONSHIPS
                    + env_params.RELATIONSHIP_ATTRIBUTE_NUM, 64),
            nn.ReLU(),
            nn.Linear(64, TARGET_ENCODING_SIZE)
        )

        env_encoding_size = env_params.ENTITY_TYPE_NUM \
                + env_params.RELATIONSHIP_TYPE_NUM \
                + TARGET_ENCODING_SIZE
        
        self.gru_cell = nn.GRUCell(env_encoding_size, 128)
        self.hidden = torch.randn(1, 128)

        self.actor = nn.Sequential(
            nn.Linear(128, env_params.THEOREM_NUM),
            nn.Softmax(dim=0)
        )

    def forward(self, x):
        entity_tensor = x['entity']
        relationship_tensor = x['relationship']
        target_tensor = x['target']
        action_mask_tensor = x['action_mask']

        entity_feature = self.entity_encoder(entity_tensor)
        relationship_feature = self.relationship_encoder(relationship_tensor)

        # Group by type.
        # And then max pooling.
        entiy_type_group = []
        for i in range(env_params.ENTITY_TYPE_NUM):
            type_tensor = []
            for row in range(env_params.MAX_ENTITIES):
                if entity_tensor[row, i] == 1:
                    type_tensor.append(entity_feature[row])
            if not type_tensor:
                type_tensor = torch.tensor(0).float().to(self.device)
            else:
                type_tensor = torch.stack(type_tensor)
                type_tensor = torch.max(type_tensor)
            entiy_type_group.append(type_tensor)
        entiy_type_group = torch.stack(entiy_type_group)

        relationship_type_group = []
        for i in range(env_params.RELATIONSHIP_TYPE_NUM):
            type_tensor = []
            for row in range(env_params.MAX_RELATIONSHIPS):
                if relationship_tensor[row, i] == 1:
                    type_tensor.append(relationship_feature[row])
            if not type_tensor:
                type_tensor = torch.tensor(0).float().to(self.device)
            else:
                type_tensor = torch.stack(type_tensor)
                type_tensor = torch.max(type_tensor)
            relationship_type_group.append(type_tensor)
        relationship_type_group = torch.stack(relationship_type_group)

        # Target encoding
        target_feature = self.target_encoder(target_tensor)

        env_feature = torch.cat([entiy_type_group, relationship_type_group, target_feature])
        
        env_feature = env_feature.view(1, -1)
        env_feature = self.gru_cell(env_feature, self.hidden)
        env_feature = env_feature.view(-1)
        logits = self.actor(env_feature)

        # Add action mask
        masked_logits = logits * action_mask_tensor

        return masked_logits

