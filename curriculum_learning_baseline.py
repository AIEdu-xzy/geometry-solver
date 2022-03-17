from typing import List
import json

from tqdm import tqdm
import numpy as np

from geometry_solver import Solver
from utils import get_practical_problems

trial_time = 10
all_problems = 130


def run_random_search(policy=None, show_process_bar=False):
    problems = get_practical_problems(range(1, 1+all_problems))

    total_trial = np.zeros(all_problems)
    total_before_prune = np.zeros(all_problems)
    total_after_prune = np.zeros(all_problems)

    for i, problem in enumerate(tqdm(problems)):
        solver = Solver(problem, policy)
        result = solver.solve(show_answer=False, show_process=False, show_graph=False, prune=True)
        total_trial[i] = result['trial_times']
        total_before_prune[i] = result['solving_steps_before_prune']
        total_after_prune[i] = result['solving_steps_after_prune']

    return total_trial, total_before_prune, total_after_prune


def get_each_problem_performance():
    all_trials = np.zeros((trial_time, all_problems))
    all_before_prune = np.zeros((trial_time, all_problems))
    all_after_prune = np.zeros((trial_time, all_problems))
    for i in range(trial_time):
        trial, before_prune, after_prune = run_random_search()
        all_trials[i, :] = trial[:]
        all_before_prune[i, :] = before_prune[:]
        all_after_prune[i, :] = after_prune[:]
        
    avg_trials = np.average(all_trials, axis=0)
    avg_before_prune = np.average(all_before_prune, axis=0)
    avg_after_prune = np.average(all_after_prune, axis=0)
    return avg_trials, avg_before_prune, avg_after_prune


def main():
    info = {}
    avg_trials, avg_before_prune, avg_after_prune = get_each_problem_performance()
    for i in range(all_problems):
        info['problem_' + str(i + 1)] = [avg_trials[i], avg_before_prune[i], avg_after_prune[i]]
    
    with open('problem_solving_step.json', 'w') as f:
        json.dump(info, f, indent=4, sort_keys=True)

if __name__ == '__main__':
    main()
