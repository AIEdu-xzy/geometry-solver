from copy import deepcopy

from tests.practical_test.practical_test5 import practical_test5
from geometry_solver import Solver
from geometry_solver.reinforcement_learning.utils import initialize_theorems


theorems = initialize_theorems()

problems = []
for i in range(1, 51):
    exec('from tests.practical_test.practical_test{} import practical_test{}'.format(i, i))
    exec('problems.append(practical_test{}())'.format(i))


problem = problems[4]
q = []
next_q = []

q.append(problem)
steps = [1]

while True:
    print(len(q))
    for p in q:
        for th in theorems:
            if p.is_valid(th):
                p_copy = deepcopy(p)
                p_copy.deduct(th)
                if p_copy.solved:
                    print('problem solved!')
                    exit(0)
                next_q.append(p_copy)
    q = next_q
    next_q = []

