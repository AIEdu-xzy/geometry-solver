from geometry_solver.reinforcement_learning.mcts_pure.mcts_pure import run_mcts
from utils import get_practical_problems


problems = get_practical_problems(range(1, 101))
run_mcts(problems)
