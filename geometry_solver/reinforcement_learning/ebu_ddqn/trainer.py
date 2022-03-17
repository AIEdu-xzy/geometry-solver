import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import gym
env = gym.make('CartPole-v1')
env.reset()

N_ACTIONS = env.action_space.n
N_STATES = env.observation_space.shape[0]

BATCH_SIZE = 1


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.linear1 = nn.Linear(N_STATES, 64)
        self.linear2 = nn.Linear(64, 16)
        self.v_linear = nn.Linear(16, 1)
        self.a_linear = nn.Linear(16, N_ACTIONS)

    def forward(self, s):
        # print(s)
        x = s.float()
        common_out = self.linear1(x)
        common_out = F.relu(common_out)
        common_out = self.linear2(common_out)
        common_out = F.relu(common_out)

        v = self.v_linear(common_out)
        a = self.a_linear(common_out)
        out = v + a
        return out


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

        self.eval_net = Net().to(device)
        self.target_net = Net().to(device)
        self.learn_step_counter = 0
        self.optimizer = torch.optim.Adam(self.eval_net.parameters(),
                lr=learning_rate)
        self.loss_func = nn.MSELoss()

        self.memory_index = 0
        self.memory = np.zeros((self.memory_capacity, N_STATES * 2 + 2))

        self.learn_step_counter = 0

        self.is_double_dqn = is_double_dqn

    def choose_action(self, s, epsilon):
        s = torch.unsqueeze(torch.FloatTensor(s), dim=0).to(self.device)
        if np.random.uniform() < epsilon:
            actions_value = self.eval_net.forward(s)
            action = torch.max(actions_value, 1)[1].data.cpu().numpy()
            action = action[0]
        else:
            action = np.random.randint(N_ACTIONS)
        return action

    def store_transition(self, s, a, r, s_next):
        index = self.memory_index % self.memory_capacity
        transition = np.hstack((s, a, r, s_next))
        self.memory[index] = transition
        self.memory_index += 1

    def learn(self):
        if self.learn_step_counter % self.target_replace_iter == 0:
            self.target_net.load_state_dict(self.eval_net.state_dict())
        self.learn_step_counter += 1

        sample_index = np.random.choice(self.memory_capacity, BATCH_SIZE)
        b_memory = self.memory[sample_index]
        b_s = torch.FloatTensor(b_memory[:, :N_STATES]).to(self.device)
        b_a = torch.LongTensor(b_memory[:, N_STATES:N_STATES+1]).to(self.device)
        b_r = torch.FloatTensor(b_memory[:, N_STATES+1:N_STATES+2]).to(self.device)
        b_s_next = torch.FloatTensor(b_memory[:, -N_STATES:]).to(self.device)

        # with torch.no_grad():
        q_eval = self.eval_net(b_s).gather(1, b_a)

        if self.is_double_dqn:
            q_eval_next = self.eval_net(b_s_next).detach()
            selected_actions = torch.argmax(q_eval_next, dim=1).view(BATCH_SIZE, 1)
            q_next = self.target_net(b_s_next).detach()
            target_value = torch.gather(q_next, 1, selected_actions)
            q_target = b_r + self.gamma * target_value
        else:
            q_next = self.target_net(b_s_next).detach()
            q_target = b_r + gamma * q_next.max(dim=1)[0].view(BATCH_SIZE, 1)

        loss = self.loss_func(q_eval, q_target)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()


class Trainer(object):

    def __init__(self, args):
        self.agent = Agent(
                args.device, args.learning_rate, args.gamma, 
                args.target_replace_iter, args.memory_capacity)
        self.training_epoch = args.training_episode
        self.epsilon = args.epsilon
        self.memory_capacity = args.memory_capacity

    def train(self):
        for i in range(self.training_epoch):
            total_reward = 0
            s = env.reset()
            while True:
                # env.render()
                a = self.agent.choose_action(s, self.epsilon)
                s_next, r, done, info = env.step(a)

                # Modify reward.
                x, x_dot, theta, theta_dot = s_next
                r1 = (env.x_threshold - abs(x)) / env.x_threshold - 0.8
                r2 = (env.theta_threshold_radians - abs(theta)) / env.theta_threshold_radians - 0.5
                r_modified = r1 + r2

                self.agent.store_transition(s, a, r_modified, s_next)

                if self.agent.memory_index > self.memory_capacity:
                    self.agent.learn()

                s = s_next
                total_reward += r
                if done:
                    # print('epoch: {}, get reward: {}'.format(i, total_reward))
                    break

            if i % 50 == 0:
                total_reward = 0
                for _ in range(50):
                    s = env.reset()
                    while True:
                        a = self.agent.choose_action(s, epsilon=1)
                        s, r, done, _ = env.step(a)
                        total_reward += r
                        if done:
                            break
                print('Epoch: {}, average reward = {}'.format(i, total_reward / 50))

        env.close()


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--learning_rate', type=float, default=0.001)
parser.add_argument('--gamma', type=float, default=0.9)
parser.add_argument('--epsilon', type=float, default=0.8)
parser.add_argument('--training_episode', type=int, default=1000)
parser.add_argument('--device', type=str, default='cpu')
parser.add_argument('--target_replace_iter', type=int, default=100)
parser.add_argument('--memory_capacity', type=int, default=2000)

args = parser.parse_args()

trainer = Trainer(args)
trainer.train()

