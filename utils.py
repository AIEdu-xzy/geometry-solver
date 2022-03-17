from typing import List

from tqdm import tqdm

from geometry_solver import Solver

ROOT = 'tests'


def get_practical_problems(ids: List[int]):
    return [get_problem(i, test_type='practical_test') for i in ids]


def get_problem(number, test_type):
    module_name = test_type + str(number)
    path = '.'.join([ROOT, test_type, module_name])
    exec('from {} import {}'.format(path, module_name))
    exec('problem = {}()'.format(module_name), locals())
    return locals()['problem']


def test_all_problems(policy=None, show_process_bar=False):
    problems = get_practical_problems(range(101, 131))

    total_trial = 0
    total_before_prune = 0
    total_after_prune = 0

    iter_obj = problems
    if show_process_bar:
        iter_obj = tqdm(iter_obj)
    for i, problem in enumerate(iter_obj):
        # print(i)
        solver = Solver(problem, policy)
        result = solver.solve(show_answer=False, show_process=False, show_graph=False, prune=True)
        total_trial += result['trial_times']
        total_before_prune += result['solving_steps_before_prune']
        total_after_prune += result['solving_steps_after_prune']

    # print('Average trial times: {}'.format(total_trial / len(problems)))
    # print('Solving step before prune {}'.format(total_before_prune / len(problems)))
    # print('Solving step after prune {}'.format(total_after_prune / len(problems)))

    avg_trial = total_trial / len(problems)
    avg_before_prune = total_before_prune / len(problems)
    avg_after_prune = total_after_prune / len(problems)

    return avg_trial, avg_before_prune, avg_after_prune
