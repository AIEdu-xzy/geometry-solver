import argparse
import gym
import numpy as np
from itertools import count
from collections import namedtuple

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical

from geometry_solver.reinforcement_learning.env import Environment
from geometry_solver.reinforcement_learning.a2c.net import Net

eps = np.finfo(np.float32).eps.item()


SavedAction = namedtuple('SavedAction', ['log_prob', 'value'])



class Agent(object):
    """
    implements both actor and critic in one model
    """
    def __init__(self, device):
        # action & reward buffer
        self.saved_actions = []
        self.rewards = []
        self.model = Net(device)
        
    def chose_action(self, state):
        probs, state_value = self.model(state)

        try:
            # create a categorical distribution over the list of probabilities of actions
            m = Categorical(probs)

            # and sample an action using the distribution
            action = m.sample()
        except:
            print(probs)
            print(state['action_mask'])
            exit(1)

        # save to action buffer
        self.saved_actions.append(SavedAction(m.log_prob(action), state_value))

        # the action to take (left or right)
        return action.item()


class Trainer(object):
    
    def __init__(self, problems, args):
        self.agent = Agent(args.device)
        self.optimizer = optim.Adam(self.agent.model.parameters(), lr=3e-2)
        self.gamma = args.gamma
        self.env = Environment(problems, args.device)
        
        self.log_interval = args.log_interval
        self.training_episode = args.training_episode
    
    def finish_episode(self):
        """
        Training code. Calculates actor and critic loss and performs backprop.
        """
        R = 0
        saved_actions = self.agent.saved_actions
        policy_losses = [] # list to save actor (policy) loss
        value_losses = [] # list to save critic (value) loss
        returns = [] # list to save the true values

        # calculate the true value using rewards returned from the environment
        for r in self.agent.rewards[::-1]:
            # calculate the discounted value
            R = r + self.gamma * R
            returns.insert(0, R)

        returns = torch.tensor(returns)
        returns = (returns - returns.mean()) / (returns.std() + eps)

        for (log_prob, value), R in zip(saved_actions, returns):
            advantage = R - value.item()

            # calculate actor (policy) loss 
            policy_losses.append(-log_prob * advantage)

            # calculate critic (value) loss using L1 smooth loss
            value_losses.append(F.smooth_l1_loss(value, torch.tensor([R])))

        # reset gradients
        self.optimizer.zero_grad()

        # sum up all the values of policy_losses and value_losses
        loss = torch.stack(policy_losses).sum() + torch.stack(value_losses).sum()

        # perform backprop
        loss.backward()
        self.optimizer.step()

        # reset rewards and action buffer
        del self.agent.rewards[:]
        del self.agent.saved_actions[:]

    def train(self):
        running_reward = 10

        # run inifinitely many episodes
        for i in range(self.training_episode):

            # reset environment and episode reward
            state = self.env.reset()
            ep_reward = 0

            # for each episode, only run 9999 steps so that we don't 
            # infinite loop while learning
            for t in range(1, 10000):

                # select action from policy
                action = self.agent.chose_action(state)

                # take the action
                state, reward, done, _ = self.env.step(action)

                self.agent.rewards.append(reward)
                ep_reward += reward
                if done:
                    break

            # update cumulative reward
            running_reward = 0.05 * ep_reward + (1 - 0.05) * running_reward

            # perform backprop
            self.finish_episode()

            # log results
            if i % self.log_interval == 0:
                print('Episode {}\tLast reward: {:.2f}\tAverage reward: {:.2f}'.format(
                    i, ep_reward, running_reward))
            
            yield self.agent


