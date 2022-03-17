import torch
import torch.nn as nn
from torch.optim import Adam
from torch.distributions import Categorical
import gym
from tqdm import tqdm
import numpy as np

from geometry_solver.reinforcement_learning.pg.net import Net
from geometry_solver.reinforcement_learning.env import Environment
from geometry_solver.policy import RLPolicy


class Agent(object):

    def __init__(self, device):
        self.net = Net(device).to(device)

    def chose_action(self, obs):
        with torch.no_grad():
            probs = self.net(obs)
            try:
                d = Categorical(probs)
                action = d.sample()
            except:
                print(probs)
                exit(1)
        return action.cpu().data.numpy().astype(int)

    def update_policy(self, obs):
        action = torch.argmax(self.net(obs))
        return action


class Trainer(object):

    def __init__(self, problems, args):
        self.training_episode = args.training_episode
        self.sample_num = args.sample_num
        self.test_num = args.test_num
        self.gamma = args.gamma
        self.show_process_bar = args.show_process_bar
        self.device = args.device

        self.env = Environment(problems,
                curriculum_learning=args.curriculum_learning,
                max_episode=args.training_episode,
                device=args.device)
        self.agent = Agent(args.device)
        self.optimizer = Adam(self.agent.net.parameters(), lr=args.learning_rate)

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
                action = agent.chose_action(obs)
                obs, reward, done, _ = env.step(action)
                total_reward += reward
                step_temp += 1
                if done:
                    break
            final_score.append(total_reward)
        print('Final score = {}'.format(sum(final_score) / len(final_score)))

    def update_policy(self, agent, state_pool, action_pool, reward_pool):
        print('Update policy...')
        self.optimizer.zero_grad()
        losses = []
        for a, s, r in zip(action_pool, state_pool, reward_pool):
            a = torch.tensor(a).long().to(self.device)
            r = torch.tensor(r).to(self.device)
            probs = agent.net(s)
            m = Categorical(probs)
            loss = -m.log_prob(a) * r
            losses.append(loss)
        batch_loss = torch.stack(losses).sum()
        batch_loss.backward()
        self.optimizer.step()

    def interaction(self, env, agent):
        # sample experience.
        print('Begin to sample...')
        state_pool = []
        action_pool = []
        reward_pool = []

        iter_obj = range(self.sample_num)
        if self.show_process_bar:
            iter_obj = tqdm(iter_obj)
        for _ in iter_obj:
            episode_state = []
            episode_action = []
            episode_reward = []
            obs = env.reset()
            while True:
                action = agent.chose_action(obs)
                episode_state.append(obs)
                episode_action.append(action)
                obs, reward, done, _ = env.step(action)
                episode_reward.append(reward)
                if done:
                    running_reward = 0
                    for i in reversed(range(len(episode_reward))):
                        running_reward += episode_reward[i]
                        episode_reward[i] = running_reward
                        running_reward *= self.gamma
                    reward_pool += episode_reward
                    state_pool += episode_state
                    action_pool += episode_action
                    break
        return state_pool, action_pool, reward_pool


    def train(self):
        agent = self.agent
        env = self.env
        for i in range(self.training_episode):
            env.episode = i
            print('Episode {}'.format(i))
            state_pool, action_pool, reward_pool = self.interaction(env, agent)
            self.update_policy(agent, state_pool, action_pool, reward_pool)
            self.test_performance(env, agent)
            yield agent

