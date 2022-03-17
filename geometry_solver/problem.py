from typing import List

from geometry_solver.entity import Entity
from geometry_solver.condition import Condition
from geometry_solver.target import Target
from geometry_solver.graph.deduction_graph import DeductionGraph
from geometry_solver.indexer.indexer import Indexer


class Problem(object):
    
    def __init__(self, entity: Entity, conditions: List[Condition], target: Target):
        if len(entity.children) == 0:
            raise ValueError("Problem entity is empty!")
        self.entity = entity
        self.conditions = conditions
        self.target = target
        # Initialize deduction graph.
        self.graph = DeductionGraph(conditions, target)
        # Build indexer
        self.indexer = Indexer(entity, self.graph)
    
    def set_entity(self, entity: Entity) -> None:
        self.entity = entity

    def set_conditions(self, conditions: List[Condition]) -> None:
        self.conditions = conditions
        
    @property
    def solved(self):
        return self.graph.solved
    
    def deduct(self, theorem):
        # Traverse all [sources, target] pair that meet requirement of theorem.
        for srcs, tg in theorem.index(self.indexer):
            srcs, tg = theorem.deduct(srcs, tg)
            # There can be multiple targets.
            if not isinstance(tg, list):
                tg = [tg]
            for tg_ in tg:
                self.graph.expand(tg_)
                tg_.from_conditions = srcs
                tg_.from_theorem = theorem
                self.indexer.update_index(tg_)
                
    def is_valid(self, theorem):
        """Determine whether the given theorem is valid."""
        return True if theorem.index(self.indexer) else False
                
    def solving_path(self):
        return self.graph.solving_path()
    
    def solving_steps(self):
        return self.graph.solving_steps()
    
    def plain_word_answer(self):
        return self.graph.plain_word_answer()
    
    def show_graph(self):
        self.graph.show_graph()
        
