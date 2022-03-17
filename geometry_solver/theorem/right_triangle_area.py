from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, AttributeValue
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.entity import Triangle
from geometry_solver.relationship import IsRightTriangle


class RightTriangleArea(Theorem):

    name = "right triangle area"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        rt_conds = indexer.index_by_type(IsRightTriangle)
        for cond in rt_conds:
            r = cond.relationship
            triangle = r.triangle
            area_cond = indexer.index_value_condition(triangle, 'area')
            # If area is already known, skip.
            if area_cond.attr_value is not None:
                continue
            leg1_cond = indexer.index_value_condition(r.legs[0], 'length')
            if leg1_cond.attr_value is None:
                continue
            leg2_cond = indexer.index_value_condition(r.legs[1], 'length')
            if leg2_cond.attr_value is None:
                continue
            ret.append([[cond, leg1_cond, leg2_cond], area_cond])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        a = sources[1].attr_value
        b = sources[2].attr_value
        target.attr_value = a * b / 2
        return sources, target

