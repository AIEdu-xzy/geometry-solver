from typing import List
import math

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import TwoSum
from geometry_solver.entity.angle import Angle
from geometry_solver.entity.line import Line
from geometry_solver.relationship.value_equivalence import ValueEquivalence


class TwoSumDeduction2(Theorem):
    
    name = "two sum deduction 2"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        two_sums = indexer.index_by_type(TwoSum)
        equal_conds = indexer.index_by_type(ValueEquivalence)
        if not equal_conds:
            return []
        for two_sum in two_sums:
            r = two_sum.relationship
            for cond in equal_conds:
                eq_r = cond.relationship
                if r.entity1 in eq_r.obj_list and r.entity2 in eq_r.obj_list:
                    idx1 = eq_r.obj_list.index(r.entity1)
                    idx2 = eq_r.obj_list.index(r.entity2)
                    if r.attr1 == eq_r.attr_list[idx1] and r.attr2 == eq_r.attr_list[idx2]:
                        cond1 = indexer.index_value_condition(r.entity1, r.attr1, False)
                        cond2 = indexer.index_value_condition(r.entity2, r.attr2, False)
                        if cond1 is None:
                            cond1 = indexer.index_value_condition(r.entity1, r.attr1)
                            ret.append([[two_sum, cond], cond1])
                        if cond2 is None:
                            cond2 = indexer.index_value_condition(r.entity2, r.attr2)
                            ret.append([[two_sum, cond], cond2])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = sources[0].relationship.sum_value / 2
        return sources, target

