from typing import List
import time

import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

from geometry_solver.indexer.indexer import Indexer
from geometry_solver.policy import BasePolicy, RandomPolicy
from geometry_solver.problem import Problem


class Solver(object):

    def __init__(self, 
            problem: Problem,
            policy: BasePolicy=None):
        self.problem = problem
        if policy is None:
            policy = RandomPolicy()
        self.policy = policy

    def solve(self,
            show_answer=True,
            show_process=True,
            show_graph=True,
            prune=True) -> None:
        """Solve the problem.

        :param show_answer: 
            if true, final answer will be printed through standard output.
        :param show_process: 
        if true, solving process will be printed through standard output.
        :param show_graph: 
            if true, deduction graph will be shown after solved.
        :prune_graph: 
            if true, the deduction graph will be pruned to remove unneccessary step.
        """
        begin = time.time()
        trial_times = 0
        # Adopt policy until solve the problem.
        while not self.problem.solved:
            theorem = self.policy.chose_theorem(self.problem)
            if show_process:
                print("trial {}: chose {}".format(trial_times, theorem.name))
            self.problem.deduct(theorem)
            trial_times += 1
        end = time.time()
        time_usage = end - begin

        solving_steps_before_prune = self.problem.solving_steps()
        solving_steps_after_prune = None

        graph = self.problem.graph
        if prune:
            graph.prune()
            solving_steps_after_prune = self.problem.solving_steps()
        
        if show_process:
            print('Problem solved succesfully!')
        
        plain_word_answer = self.problem.plain_word_answer()
        if show_answer:
            print(plain_word_answer)

        if show_graph:
            self.problem.show_graph()
        
        result = {
            "plain_word_answer": plain_word_answer,
            "solving_steps_before_prune": solving_steps_before_prune,
            "solving_steps_after_prune": solving_steps_after_prune,
            "trial_times": trial_times,
            "time_usage": time_usage,
            "answer": graph.answer
        }
        return result

