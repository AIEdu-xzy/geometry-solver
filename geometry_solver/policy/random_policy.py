import numpy as np

from geometry_solver.policy.base_policy import BasePolicy


class RandomPolicy(BasePolicy):

    def __init__(self):
        super().__init__()

    def chose_theorem(self, problem):
        theorem = np.random.choice(self.theorems)
        return theorem

