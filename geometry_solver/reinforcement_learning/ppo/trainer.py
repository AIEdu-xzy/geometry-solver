from collections import namedtuple

import torch
import torch.nn as nn
from torch.optim import Adam
import torch.nn.functional as F
from torch.distributions import Categorical
import gym
import numpy as np


class Net(nn.Module):

    def __init__(self):
        super().__init__()
        self.affine = nn.Sequential(
            nn.Linear(4, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU()
        ).float()
        self.action_layer = nn.Sequential(
            nn.Linear(32, 2),
            nn.Softmax(dim=0)
        ).float()
        self.value_layer = nn.Sequential(
            nn.Linear(32, 1)
        ).float()

    def forward(self, x):
        if not torch.is_tensor(x):
            x = torch.tensor(x)
        x = x.float()
        x = self.affine(x)

        state_value = self.value_layer(x)
        action_probs = self.action_layer(x)
        return action_probs, state_value


Transition = namedtuple('Transition',
        ('state', 'action', 'log_prob', 'reward', 'done'))

class Memory(object):

    def __init__(self, capacity):
        self.memory = [0] * capacity
        self.capacity = capacity
        self.index = 0

    def push(self, transition):
        self.memory[self.index % self.capacity] = transition
        self.index += 1

    def sample(self):
        states = []
        rewards = []
        actions = []
        logprobs = []
        is_terminals = []
        for t in self.memory:
            states.append(t.state)
            rewards.append(t.reward)
            actions.append(t.action)
            logprobs.append(t.log_prob)
            is_terminals.append(t.done)
        return states, rewards, actions, logprobs, is_terminals


class Agent(object):

    def __init__(self, device):
        self.net = Net()

    def chose_action(self, obs):
        probs, value = self.net(obs)
        d = Categorical(probs)
        action = d.sample()
        return action.cpu().data.numpy().astype(int), d.log_prob(action), value

    def evaluate(self, obs, action):
        probs, value = self.net(obs)
        d = Categorical(probs)
        action_logprobs = d.log_prob(action)
        dist_entropy = d.entropy()

        return action_logprobs, torch.squeeze(value), dist_entropy


class Trainer(object):

    def __init__(self, args):
        self.training_episode = args.training_episode
        self.sample_num = args.sample_num
        self.test_num = args.test_num
        self.gamma = args.gamma
        self.show_process_bar = args.show_process_bar
        self.device = args.device
        self.eps_clip = args.eps_clip

        self.env = gym.make('CartPole-v1')
        self.policy = Agent(args.device)
        self.policy_old = Agent(args.device)
        self.policy_old.net.load_state_dict(self.policy.net.state_dict())
        self.optimizer = Adam(self.policy.net.parameters(), lr=args.learning_rate)
        self.MseLoss = nn.MSELoss()

        self.memory = Memory(args.memory_capacity)

    def test_performance(self, env, agent):
        print('Test performance...')
        final_score = []

        iter_obj = range(self.test_num)
        if self.show_process_bar:
            iter_obj = tqdm(iter_obj)
        for _ in iter_obj:
            obs = env.reset()
            total_reward = 0
            step_temp = 0
            while True:
                action, _, _ = agent.chose_action(obs)
                obs, reward, done, _ = env.step(action)
                total_reward += reward
                step_temp += 1
                if done:
                    break
            final_score.append(total_reward)
        print('Final score = {}'.format(sum(final_score) / len(final_score)))

    def update_policy(self, memory_states, memory_rewards,
                memory_actions, memory_logprobs, memory_is_terminals):
        print('Update policy...')

        rewards = []
        discounted_reward = 0
        for reward, is_terminal in zip(reversed(memory_rewards), reversed(memory_is_terminals)):
            if is_terminal:
                discounted_reward = 0
            discounted_reward = reward + (self.gamma * discounted_reward)
            rewards.insert(0, discounted_reward)
        # Normalizing the rewards:
        rewards = torch.tensor(rewards, dtype=torch.float32)
        rewards = (rewards - rewards.mean()) / (rewards.std() + 1e-5)

        # convert list to tensor
        old_states = torch.from_numpy(np.asarray(memory_states)).detach()
        old_actions = torch.from_numpy(np.asarray(memory_actions)).detach()
        old_logprobs = torch.stack(memory_logprobs).detach()

        # Evaluating old actions and values :
        logprobs, state_values, dist_entropy = self.policy.evaluate(old_states, old_actions)

        # Finding the ratio (pi_theta / pi_theta__old):
        ratios = torch.exp(logprobs - old_logprobs.detach())

        # Finding Surrogate Loss:
        advantages = rewards - state_values.detach()
        surr1 = ratios * advantages
        surr2 = torch.clamp(ratios, 1-self.eps_clip, 1+self.eps_clip) * advantages
        loss = -torch.min(surr1, surr2) + 0.5*self.MseLoss(state_values, rewards) - 0.01*dist_entropy

        # take gradient step
        self.optimizer.zero_grad()
        loss.mean().backward()
        self.optimizer.step()

        self.policy_old.net.load_state_dict(self.policy.net.state_dict())

    def interaction(self, env, agent, memory):
        # sample experience.
        print('Begin to sample...')

        iter_obj = range(self.sample_num)
        if self.show_process_bar:
            iter_obj = tqdm(iter_obj)
        for _ in iter_obj:
            obs = env.reset()
            while True:
                action, log_prob, value = agent.chose_action(obs)
                next_obs, reward, done, _ = env.step(action)
                transition = Transition(state=obs, action=action,
                        log_prob=log_prob, reward=reward, done=done)
                memory.push(transition)
                obs = next_obs
                if done:
                    break

    def train(self):
        env = self.env
        for i in range(self.training_episode):
            print('Episode {}'.format(i))
            self.interaction(env, self.policy_old, self.memory)
            if self.memory.index >= self.memory.capacity:
                states, rewards, actions, logprobs, is_terminals = self.memory.sample()
                self.update_policy(states, rewards, actions, logprobs, is_terminals)
            self.test_performance(env, self.policy)
            # yield agent

import argparse
parser = argparse.ArgumentParser(description='ArgumentParser for reinforcement '
        'learning training configuration.')
parser.add_argument('--training_episode', type=int, default=100)
parser.add_argument('--learning_rate', type=float, default=0.01)
parser.add_argument('--gamma', type=float, default=0.99)
parser.add_argument('--sample_num', type=int, default=1)
parser.add_argument('--test_num', type=int, default=10)
parser.add_argument('--device', type=str, default='cpu')
parser.add_argument('--show_process_bar', action='store_true')
parser.add_argument('--memory_capacity', type=int, default=2000)
parser.add_argument('--eps_clip', type=float, default=0.2)

args = parser.parse_args()

trainer = Trainer(args)
trainer.train()
