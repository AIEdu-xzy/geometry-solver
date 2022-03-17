from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import NLineSector
from geometry_solver.entity import Triangle
from geometry_solver.common.utils import attr_value_known_num


class NLineSectorProportional(Theorem):

    name = "n line sector proportional"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        nls_conds = indexer.index_by_type(NLineSector)
        for cond in nls_conds:
            r = cond.relationship
            # Existence of ratio condition is guaranteed.
            ratio_cond = indexer.index_value_condition(r, 'ratio')
            ratio = ratio_cond.attr_value
            
            near_point, split_point, far_point = r.three_points
            line_near = indexer.index_line_by_points(near_point, split_point)
            line_far = indexer.index_line_by_points(far_point, split_point)
            line_full = indexer.index_line_by_points(near_point, far_point)
            
            near_cond = indexer.index_value_condition(line_near, 'length')
            far_cond = indexer.index_value_condition(line_far, 'length')
            full_cond = indexer.index_value_condition(line_full, 'length')
            
            if full_cond.attr_value is None:
                if near_cond.attr_value is not None:
                    ret.append([[near_cond, ratio_cond, 1/ratio], full_cond])
                elif far_cond.attr_value is not None:
                    ret.append([[far_cond, ratio_cond, 1/(1-ratio)], full_cond])
            if near_cond.attr_value is None:
                if full_cond.attr_value is not None:
                    ret.append([[full_cond, ratio_cond, ratio], near_cond])
                elif far_cond.attr_value is not None:
                    ret.append([[far_cond, ratio_cond, ratio/(1-ratio)], near_cond])
            if far_cond.attr_value is None:
                if full_cond.attr_value is not None:
                    ret.append([[full_cond, ratio_cond, 1-ratio], far_cond])
                elif near_cond.attr_value is not None:
                    ret.append([[near_cond, ratio_cond, (1-ratio)/ratio], far_cond])

        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        ratio = sources[-1]
        target.attr_value = sources[0].attr_value * ratio
        return sources[:-1], target

