from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import IsRightTriangle
from geometry_solver.entity import Triangle


class RightTriangleJudgment(Theorem):

    name = "right triangle judgment"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        r_conds = indexer.index_by_type(IsRightTriangle)
        triangles = indexer.index_by_type(Triangle)
        right_triangles = [cond.relationship.triangle for cond in r_conds]

        for th in triangles:
            if th in right_triangles:
                continue
            for angle in [th.angle1, th.angle2, th.angle3]:
                a_cond = indexer.index_value_condition(angle, 'angle')
                if a_cond.attr_value is not None and a_cond.attr_value == 90:
                    rt = IsRightTriangle(th.id, th, angle)
                    rt_cond = RelationshipBased(rt)
                    ret.append([[a_cond], rt_cond])
                    break
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        # RT triangle condition is target, don't need to deduct.
        return sources, target

