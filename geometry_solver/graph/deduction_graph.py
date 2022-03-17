from typing import List

import networkx as nx
import matplotlib.pyplot as plt

from geometry_solver.target.target import Target
from geometry_solver.condition import Condition, AttributeValue
from geometry_solver.config import ROUND_PRECISION


class DeductionGraph(object):
    
    def __init__(self, 
            conditions: List[Condition],
            target: Target):
        self.conditions = conditions
        self.attr_value_conds = \
                [c for c in conditions if type(c) == AttributeValue]
        self.target = target
        self.solved = self._target_solved(conditions, target)
        self.target_node = None

    def expand(self, new_condition: Condition):
        """Expand graph after one step deduction.

        :param new_condition: a new condition add to graph.
        """
        self.conditions.append(new_condition)
        if type(new_condition) == AttributeValue:
            self.attr_value_conds.append(new_condition)
        
        if not self.solved \
                and self._target_solved([new_condition], self.target):
            self.target_node = new_condition
            self.solved = True

    def _target_solved(self, 
            conditions: List[Condition], 
            target: Target):
        """Traversal the conditions, find if there is a condition match target.
        
        Return true if there is a condition match the target.
        """
        for cond in conditions:
            if cond.match(target):
                return True
        return False

    def solving_path(self):
        if self.target_node is None:
            return """The problem is solved!"""
        return self._solving_path(self.target_node)

    def _solving_path(self, node):
        if not node.from_conditions:
            return []
        path = []
        for cond in node.from_conditions:
            path += self._solving_path(cond)
        preconditions = node.from_conditions
        theorem = node.from_theorem
        result = node
        triplet = (preconditions, theorem, result)
        path += [triplet]
        return path

    def show_graph(self):
        self._show_graph(self.conditions)
        
    def _show_graph(self, conditions):
        G = nx.DiGraph()
        for cond in conditions:
            G.add_node(cond)
        for cond in conditions:
            for src in cond.from_conditions:
                G.add_edge(src, cond)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()
        
    def prune(self):
        if self.target_node is None:
            raise ValueError("The problem is solved!")
        self.conditions = self._prune(self.target_node, set())
        
    def _prune(self, condition, visited):
        """Prune the graph and return pruned condition list."""
        if not condition.from_conditions:
            return [condition]
        useful_conditions = [condition]
        for cond in condition.from_conditions:
            if cond not in visited:
                visited.add(cond)
                useful_conditions += self._prune(cond, visited)
        return useful_conditions

    def plain_word_answer(self):
        """Convert deduction process to nature language."""
        if self.target_node is None:
            return 'Problem not solved.'
        answer = []
        path = self.solving_path()
        for step in path:
            # step is triplet ([preconditions], theorem, result)
            preconditions, theorem, result = step
            pre_str = ', '.join([str(pre) for pre in preconditions])
            th_str = theorem.name
            res_str = str(result)
            line = '由于 {}，根据定理 {}，推得 {}'.format(pre_str, th_str, res_str)
            answer.append(line)
        return '\n'.join(answer)

    def solving_steps(self):
        step = 0
        for cond in self.conditions:
            if cond.from_conditions:
                step += 1
        return step
    
    @property
    def answer(self):
        if not self.target_node:
            return None
        value = round(self.target_node.attr_value, ROUND_PRECISION)
        return value
