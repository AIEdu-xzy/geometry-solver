from typing import List
import random
import copy
import math

import gym
from gym.spaces.discrete import Discrete
import torch
from torch.distributions import Categorical

from geometry_solver.problem import Problem
from geometry_solver.theorem import Theorem
from geometry_solver.reinforcement_learning.utils import state_encoding, initialize_theorems
from geometry_solver.reinforcement_learning.utils import normal_distribution_value

class Environment(gym.Env):

    def __init__(self,
            problems: List[Problem],
            curriculum_learning=False,
            max_episode=0,
            device='cpu'):
        self.problem_candidates = problems
        self.theorems = initialize_theorems()
        self.action_space = Discrete(len(self.theorems))
        self.curriculum_learning = curriculum_learning
        self.device = device

        self.max_episode = max_episode
        self.episode = 0

        self.reset()

    def reset(self, problem_id=None):
        if problem_id is not None:
            self.problem = copy.deepcopy(self.problem_candidates[problem_id-1])
        else:
            self.problem = self.chose_problem()
        return state_encoding(self.problem, self.device, None)

    def step(self, action):
        """action is the index of theorem list."""
        action = int(action)
        theorem = self.theorems[action]
        self.problem.deduct(theorem)
        obs = state_encoding(self.problem, self.device, action)
        done = self.problem.solved
        reward = 100 if done else -1
        info = {}
        return obs, reward, done, info

    def render(self, mode='human'):
        """
            - human: show deduction graph.
            - rgb_array: show encoded state.
            - ansi: show plain word answer.
        """
        if self.problem is None:
            print('Problem is not solved!')
        if mode == 'human':
            self.problem.graph.show_graph()
        elif mode == 'rgb_array':
            print(state_encoding(self.problem))
        elif mode == 'ansi':
            print(self.problem.plain_word_answer)

    def close(self):
        pass

    def seed(self, seed=None):
        """Sets the seed for this env's random number generator(s).
        Note:
            Some environments use multiple pseudorandom number generators.
            We want to capture all such seeds used in order to ensure that
            there aren't accidental correlations between multiple generators.
        Returns:
            list<bigint>: Returns the list of seeds used in this env's random
              number generators. The first value in the list should be the
              "main" seed, or the value which a reproducer should pass to
              'seed'. Often, the main seed equals the provided 'seed', but
              this won't be true if seed=None, for example.
        """
        return


    def chose_problem(self):
        if self.curriculum_learning:
            mu = self.episode // self.max_episode
            std = 1
            probs = []
            for x in range(len(self.problem_candidates)):
                probs.append(normal_distribution_value(x, mu, std))
            probs = torch.tensor(probs)
            d = Categorical(probs)
            index = d.sample()
            problem = self.problem_candidates[index]
        else:
            problem = random.choice(self.problem_candidates)
        return copy.deepcopy(problem)

