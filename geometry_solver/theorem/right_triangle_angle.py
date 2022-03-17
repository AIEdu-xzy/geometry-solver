from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, AttributeValue
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.entity import Triangle
from geometry_solver.relationship import IsRightTriangle


class RightTriangleAngle(Theorem):

    name = "right triangle area"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        rt_conds = indexer.index_by_type(IsRightTriangle)
        for cond in rt_conds:
            r = cond.relationship
            angle = r.right_angle
            angle_cond = indexer.index_value_condition(angle, 'angle')
            if angle_cond.attr_value is None:
                ret.append([[cond], angle_cond])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = 90
        return sources, target

