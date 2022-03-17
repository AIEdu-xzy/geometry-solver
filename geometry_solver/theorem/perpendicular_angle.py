from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, AttributeValue
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import Perpendicular


class PerpendicularAngle(Theorem):

    name = "perpendicular angle"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        conds = indexer.index_by_type(Perpendicular)
        for cond in conds:
            r = cond.relationship
            line1 = r.line1
            line2 = r.line2
            if r.foot_point is None:
                r.foot_point = indexer.index_line_intersection(line1, line2)
            foot_point = r.foot_point
            for p1 in [line1.end1, line1.end2]:
                for p2 in [line2.end1, line2.end2]:
                    if p1 == foot_point or p2 == foot_point:
                        continue
                    angle = indexer.index_angle_by_points(p1, foot_point, p2)
                    angle_cond = indexer.index_value_condition(angle, 'angle')
                    if angle_cond.attr_value is None:
                        ret.append([[cond], AttributeValue(angle, **{'angle': None})])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = 90
        return sources, target

