import torch
import torch.nn as nn
from torch.distributions import Categorical
import gym


class Memory(object):
    def __init__(self):
        self.actions = []
        self.states = []
        self.logprobs = []
        self.rewards = []
        self.is_terminals = []

    def clear_memory(self):
        del self.actions[:]
        del self.states[:]
        del self.logprobs[:]
        del self.rewards[:]
        del self.is_terminals[:]


class ActorCritic(nn.Module):
    def __init__(self):
        super().__init__()
        self.affine = nn.Sequential(
            nn.Linear(4, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU()
        )
        self.action_layer = nn.Sequential(
            nn.Linear(32, 2),
            nn.Softmax(dim=0)
        )
        self.value_layer = nn.Sequential(
            nn.Linear(32, 1)
        )

    def forward(self):
        raise NotImplementedError

    def chose_action(self, state, memory):
        state = torch.from_numpy(state).float()
        memory.states.append(state)
        state = self.affine(state)
        action_probs = self.action_layer(state)
        dist = Categorical(action_probs)
        action = dist.sample()

        memory.actions.append(action)
        memory.logprobs.append(dist.log_prob(action))

        return action.item()

    def evaluate(self, state, action):
        state = self.affine(state)
        action_probs = self.action_layer(state)
        dist = Categorical(action_probs)

        action_logprobs = dist.log_prob(action)
        dist_entropy = dist.entropy()

        state_value = self.value_layer(state)

        return action_logprobs, torch.squeeze(state_value), dist_entropy


class Agent(object):
    def __init__(self, lr, gamma, K_epochs, eps_clip):
        self.lr = lr
        self.gamma = gamma
        self.eps_clip = eps_clip
        self.K_epochs = K_epochs

        self.policy = ActorCritic()
        self.optimizer = torch.optim.Adam(self.policy.parameters(), lr=lr)
        self.policy_old = ActorCritic()
        self.policy_old.load_state_dict(self.policy.state_dict())

        self.MseLoss = nn.MSELoss()

    def chose_action(self, state):
        state = torch.from_numpy(state).float()
        state = self.policy.affine(state)
        probs = self.policy.action_layer(state)
        d = Categorical(probs)
        action = d.sample()
        return action.item()

    def update(self, memory):
        # Monte Carlo estimate of state rewards:
        rewards = []
        discounted_reward = 0
        for reward, is_terminal in zip(reversed(memory.rewards), reversed(memory.is_terminals)):
            if is_terminal:
                discounted_reward = 0
            discounted_reward = reward + (self.gamma * discounted_reward)
            rewards.insert(0, discounted_reward)

        # Normalizing the rewards:
        rewards = torch.tensor(rewards, dtype=torch.float32)
        rewards = (rewards - rewards.mean()) / (rewards.std() + 1e-5)

        # convert list to tensor
        old_states = torch.stack(memory.states).detach()
        old_actions = torch.stack(memory.actions).detach()
        old_logprobs = torch.stack(memory.logprobs).detach()

        # Optimize policy for K epochs:
        for _ in range(self.K_epochs):
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

        # Copy new weights into old policy:
        self.policy_old.load_state_dict(self.policy.state_dict())


class Trainer(object):

    def __init__(self, args):
        self.env = gym.make('CartPole-v1')
        self.training_episode = args.training_episode
        self.max_timesteps = 300
        self.update_timestep = 2000
        self.lr = args.learning_rate
        self.gamma = args.gamma
        self.K_epochs = 4
        self.eps_clip = 0.2
        random_seed = None

        if random_seed:
            torch.manual_seed(random_seed)
            env.seed(random_seed)

    def test_performance(self, agent, env):
        env = gym.make('CartPole-v1')
        final_score = []
        for i in range(10):
            obs = env.reset()
            total_reward = 0
            while True:
                action = agent.chose_action(obs)
                obs, reward, done, _ = env.step(action)
                total_reward += reward
                if done:
                    break
            final_score.append(total_reward)
        print('Final score = {}'.format(sum(final_score) / len(final_score)))

    def train(self):
        memory = Memory()
        ppo = Agent(self.lr, self.gamma, self.K_epochs, self.eps_clip)

        # logging variables
        running_reward = 0
        avg_length = 0
        timestep = 0

        # training loop
        for i_episode in range(1, self.training_episode+1):
            state = self.env.reset()
            for t in range(self.max_timesteps):
                timestep += 1

                # Running policy_old:
                action = ppo.policy_old.chose_action(state, memory)
                state, reward, done, _ = self.env.step(action)

                # Saving reward and is_terminal:
                memory.rewards.append(reward)
                memory.is_terminals.append(done)

                # update if its time
                if timestep % self.update_timestep == 0:
                    print('episode {}'.format(i_episode))
                    ppo.update(memory)
                    memory.clear_memory()
                    timestep = 0
                    self.test_performance(ppo, self.env)

                running_reward += reward
                if done:
                    break

            avg_length += t


import argparse
parser = argparse.ArgumentParser(description='ArgumentParser for reinforcement '
        'learning training configuration.')
parser.add_argument('--training_episode', type=int, default=50000)
parser.add_argument('--learning_rate', type=float, default=0.001)
parser.add_argument('--gamma', type=float, default=0.9)
parser.add_argument('--sample_num', type=int, default=100)
parser.add_argument('--test_num', type=int, default=10)
parser.add_argument('--device', type=str, default='cpu')
parser.add_argument('--show_process_bar', action='store_true')
parser.add_argument('--memory_capacity', type=int, default=2000)

args = parser.parse_args()

trainer = Trainer(args)
trainer.train()

