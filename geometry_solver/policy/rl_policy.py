import numpy as np

from geometry_solver.policy.base_policy import BasePolicy
from geometry_solver.reinforcement_learning.utils import state_encoding


class RLPolicy(BasePolicy):

    def __init__(self, agent, device):
        super().__init__()
        self.agent = agent
        self.device = device
        self.last_step = None

    def chose_theorem(self, problem):
        obs = state_encoding(problem, self.device, self.last_step)
        theorem_id = self.agent.chose_action(obs)
        self.last_step = theorem_id
        return self.theorems[theorem_id]

