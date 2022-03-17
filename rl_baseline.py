from tqdm import tqdm
import numpy as np

from utils import get_practical_problems
from geometry_solver import Solver

avg_trial_hist = []
avg_before_prune_hist = []
avg_after_prune_hist = []


def test_all_problems():
    problems = get_practical_problems(range(1, 131))

    total_trial = 0
    total_before_prune = 0
    total_after_prune = 0

    for problem in tqdm(problems):
        solver = Solver(problem)
        result = solver.solve(show_answer=False, show_process=False, show_graph=False, prune=True)
        total_trial += result['trial_times']
        total_before_prune += result['solving_steps_before_prune']
        total_after_prune += result['solving_steps_after_prune']

    # print('Average trial times: {}'.format(total_trial / len(problems)))
    # print('Solving step before prune {}'.format(total_before_prune / len(problems)))
    # print('Solving step after prune {}'.format(total_after_prune / len(problems)))
    
    avg_trial_hist.append(total_trial / len(problems))
    avg_before_prune_hist.append(total_before_prune / len(problems))
    avg_after_prune_hist.append(total_after_prune / len(problems))


for _ in range(100):
    test_all_problems()

print(avg_trial_hist)
print(avg_before_prune_hist)
print(avg_after_prune_hist)

print('Average trial times: {}±{}'.format(np.mean(avg_trial_hist), np.std(avg_trial_hist)))
print('Average solving step before prune: {}±{}'.format(np.mean(avg_before_prune_hist), np.std(avg_before_prune_hist)))
print('Average solving step after prune: {}±{}'.format(np.mean(avg_after_prune_hist), np.std(avg_after_prune_hist)))

