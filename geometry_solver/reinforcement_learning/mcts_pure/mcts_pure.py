import os
import gym
import sys
import random
import itertools
from time import time
from copy import deepcopy
from math import sqrt, log

from tqdm import tqdm

from geometry_solver.reinforcement_learning.env import Environment


def moving_average(v, n):
    n = min(len(v), n)
    ret = [.0]*(len(v)-n+1)
    ret[0] = float(sum(v[:n]))/n
    for i in range(len(v)-n):
        ret[i+1] = ret[i] + float(v[n+i] - v[i])/n
    return ret


def ucb(node):
    return node.value / node.visits + sqrt(log(node.parent.visits)/node.visits)


def combinations(space):
    if isinstance(space, gym.spaces.Discrete):
        return range(space.n)
    elif isinstance(space, gym.spaces.Tuple):
        return itertools.product(*[combinations(s) for s in space.spaces])
    else:
        raise NotImplementedError


class Node(object):
    def __init__(self, parent, action):
        self.parent = parent
        self.action = action
        self.children = []
        self.explored_children = 0
        self.visits = 0
        self.value = 0


class Runner(object):
    
    def __init__(self, env, loops=300, max_depth=1000, playouts=10000):
        self.env = env
        self.loops = loops
        self.max_depth = max_depth
        self.playouts = playouts

    def print_stats(self, loop, score, avg_time):
        print('\r%3d   score:%10.3f   avg_time:%4.1f s' % (loop, score, avg_time))

    def run(self):
        best_rewards = []
        start_time = time()
        env = deepcopy(self.env)

        for loop in range(self.loops):
            env.reset()
            root = Node(None, None)

            best_actions = []
            best_reward = float("-inf")

            for _ in tqdm(range(self.playouts)):
                state = deepcopy(env)
                sum_reward = 0
                node = root
                terminal = False
                actions = []

                # selection
                while node.children:
                    if node.explored_children < len(node.children):
                        child = node.children[node.explored_children]
                        node.explored_children += 1
                        node = child
                    else:
                        node = max(node.children, key=ucb)
                    _, reward, terminal, _ = state.step(node.action)
                    sum_reward += reward
                    actions.append(node.action)

                # expansion
                if not terminal:
                    node.children = [Node(node, a) for a in combinations(state.action_space)]
                    random.shuffle(node.children)

                # playout
                while not terminal:
                    action = state.action_space.sample()
                    _, reward, terminal, _ = state.step(action)
                    sum_reward += reward
                    actions.append(action)

                    if len(actions) > self.max_depth:
                        sum_reward -= 100
                        break

                # remember best
                if best_reward < sum_reward:
                    best_reward = sum_reward
                    best_actions = actions

                # backpropagate
                while node:
                    node.visits += 1
                    node.value += sum_reward
                    node = node.parent

            sum_reward = 0
            for action in best_actions:
                _, reward, terminal, _ = env.step(action)
                print(f'action = {action}, reward = {reward}, is_terminal = {terminal}')
                sum_reward += reward
                if terminal:
                    break

            best_rewards.append(sum_reward)
            score = max(moving_average(best_rewards, 100))
            avg_time = (time()-start_time)/(loop+1)
            self.print_stats(loop+1, score, avg_time)


def run_mcts(problems):
    env = Environment(problems)
    # env = gym.make('CartPole-v1')
    Runner(env, loops=1, playouts=200, max_depth=200).run()


if __name__ == "__main__":
    run_mcts()
