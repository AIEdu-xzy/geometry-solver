from typing import List
import math

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import TwoSum


class TwoSumDeduction1(Theorem):
    
    name = "two sum deduction 1"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        two_sums = indexer.index_by_type(TwoSum)
        for two_sum in two_sums:
            r = two_sum.relationship
            cond1 = indexer.index_value_condition(r.entity1, r.attr1, False)
            cond2 = indexer.index_value_condition(r.entity2, r.attr2, False)
            if cond1 is None and cond2 is not None:
                cond1 = indexer.index_value_condition(r.entity1, r.attr1)
                ret.append([[two_sum, cond2], cond1])
            elif cond1 is not None and cond2 is None:
                cond2 = indexer.index_value_condition(r.entity2, r.attr2)
                ret.append([[two_sum, cond1], cond2])
                
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = sources[0].relationship.sum_value - sources[1].attr_value
        return sources, target

