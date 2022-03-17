from geometry_solver import ProblemParser
from geometry_solver import Solver

parser = ProblemParser()
problem = parser.parse('/Users/nikoyou/Desktop/解题重构/dataset/114.txt')
solver = Solver(problem)
solver.solve()
