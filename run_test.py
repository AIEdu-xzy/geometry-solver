import argparse

from geometry_solver import Solver

parser = argparse.ArgumentParser(description='ArgumentParser for test runner.')
parser.add_argument('--number', type=int)

args = parser.parse_args()

exec('from tests.practical_test.practical_test{} import practical_test{}'.format(
        args.number, args.number))
exec('problem = practical_test{}()'.format(args.number))

solver = Solver(problem)
result = solver.solve(show_answer=True, show_process=True, show_graph=True, prune=True)
print(result)

