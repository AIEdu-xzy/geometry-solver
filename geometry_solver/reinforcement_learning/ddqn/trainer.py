import random

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import gym

from geometry_solver.reinforcement_learning.env import Environment
import geometry_solver.reinforcement_learning.env_params as env_params
from geometry_solver.reinforcement_learning.ddqn.net import Net


class Agent():

    def __init__(self, 
            device, 
            learning_rate, 
            gamma, 
            target_replace_iter,
            memory_capacity,
            is_double_dqn=True):
        self.device = device
        self.gamma = gamma
        self.target_replace_iter = target_replace_iter
        self.memory_capacity = memory_capacity

        self.eval_net = Net(device).to(device)
        self.target_net = Net(device).to(device)
        self.learn_step_counter = 0
        self.optimizer = torch.optim.Adam(self.eval_net.parameters(),
                lr=learning_rate)
        self.loss_func = nn.MSELoss()

        self.memory_index = 0
        self.memory = [0] * self.memory_capacity

        self.learn_step_counter = 0

        self.is_double_dqn = is_double_dqn

    def chose_action(self, s, epsilon=1):
        if np.random.uniform() < epsilon:
            actions_value = self.eval_net.forward(s)
            action = torch.argmax(actions_value).detach().numpy()
        else:
            action = np.random.randint(env_params.THEOREM_NUM)
        return action

    def store_transition(self, s, a, r, s_next):
        index = self.memory_index % self.memory_capacity
        transition = tuple([s, a, r, s_next])
        self.memory[index] = transition
        self.memory_index += 1

    def learn(self):
        if self.learn_step_counter % self.target_replace_iter == 0:
            self.target_net.load_state_dict(self.eval_net.state_dict())
        self.learn_step_counter += 1
        
        # sample_index = np.random.choice(self.memory_capacity, BATCH_SIZE)
        # b_memory = self.memory[sample_index]
        b_memory = random.choice(self.memory)
        state, action, reward, next_state = b_memory

        b_s = state
        b_a = action
        b_r = reward
        b_s_next = next_state

        # with torch.no_grad():
        q_eval = self.eval_net(b_s)[b_a]

        if self.is_double_dqn:
            q_eval_next = self.eval_net(b_s_next).detach()
            selected_action = torch.argmax(q_eval_next, dim=0)
            q_next = self.target_net(b_s_next).detach()
            target_value = q_next[selected_action]
            q_target = b_r + self.gamma * target_value
        else:
            q_next = self.target_net(b_s_next).detach()
            q_target = b_r + gamma * q_next.max(dim=0)

        loss = self.loss_func(q_eval, q_target)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()


class Trainer(object):

    def __init__(self, problems, args):
        self.agent = Agent(
                args.device, args.learning_rate, args.gamma, 
                args.target_replace_iter, args.memory_capacity)
        self.training_epoch = args.training_episode
        self.epsilon = args.epsilon
        self.memory_capacity = args.memory_capacity
        self.env = Environment(problems, device=args.device)

    def train(self):
        begin_to_learn = False
        for i in range(self.training_epoch):
            total_reward = 0
            s = self.env.reset()
            print('Episode {}'.format(i))
            while True:
                # env.render()
                a = self.agent.chose_action(s, self.epsilon)
                s_next, r, done, info = self.env.step(a)
                self.agent.store_transition(s, a, r, s_next)

                if self.agent.memory_index > self.memory_capacity:
                    begin_to_learn = True
                    self.agent.learn()

                s = s_next
                total_reward += r
                if done:
                    # print('epoch: {}, get reward: {}'.format(i, total_reward))
                    break
            
            print('Finish episode {}'.format(i))
            
            # if begin_to_learn: 
            yield self.agent

        self.env.close()



