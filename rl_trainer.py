import argparse

import numpy as np

from utils import test_all_problems, get_practical_problems
from geometry_solver.reinforcement_learning.pg.trainer import Trainer
from geometry_solver.policy import RLPolicy

parser = argparse.ArgumentParser(description='ArgumentParser for reinforcement '
        'learning training configuration.')
parser.add_argument('--algorithm', type=str)
parser.add_argument('--training_episode', type=int, default=200)
parser.add_argument('--learning_rate', type=float, default=0.0008)
parser.add_argument('--gamma', type=float, default=0.9)
parser.add_argument('--sample_num', type=int, default=100)
parser.add_argument('--test_num', type=int, default=10)
parser.add_argument('--device', type=str, default='cpu')
parser.add_argument('--show_process_bar', action='store_true')
parser.add_argument('--log_interval', type=int, default=1)
parser.add_argument('--epsilon', type=float, default=0.8)
parser.add_argument('--target_replace_iter', type=int, default=10)
parser.add_argument('--memory_capacity', type=int, default=2000)
parser.add_argument('--curriculum_learning', action='store_true')


args = parser.parse_args()


exec('from geometry_solver.reinforcement_learning.{}.trainer import Trainer'.format(
        args.algorithm))


def test_rl_performance(agent):
    print('Testing all problems...')
    avg_trial_hist = []
    avg_before_prune_hist = []
    avg_after_prune_hist = []

    policy = RLPolicy(agent, args.device)
    for _ in range(5):
        avg_trial, avg_before_prune, avg_after_prune = test_all_problems(
            policy,
            args.show_process_bar)
        avg_trial_hist.append(avg_trial)
        avg_before_prune_hist.append(avg_before_prune)
        avg_after_prune_hist.append(avg_after_prune)

    # print(avg_trial_hist)
    # print(avg_before_prune_hist)
    # print(avg_after_prune_hist)

    print('Average trial times: {}±{}'.format(np.mean(avg_trial_hist), np.std(avg_trial_hist)))
    print('Average solving step before prune: {}±{}'.format(np.mean(avg_before_prune_hist), np.std(avg_before_prune_hist)))
    print('Average solving step after prune: {}±{}'.format(np.mean(avg_after_prune_hist), np.std(avg_after_prune_hist)))


problems = get_practical_problems(range(1, 101))
trainer = Trainer(problems, args)

for agent in trainer.train():
    test_rl_performance(agent)

