from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import IsIsoscelesTriangle
from geometry_solver.entity import Triangle


class IsoscelesTriangleJudgment1(Theorem):

    name = "isosceles triangle judgment 1"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        i_conds = indexer.index_by_type(IsIsoscelesTriangle)
        triangles = indexer.index_by_type(Triangle)
        isosceles_triangles = [cond.relationship.triangle for cond in i_conds]

        for th in triangles:
            if th in isosceles_triangles:
                continue
            permutaton = [(th.angle1, th.angle2, th.vertex3), \
                          (th.angle1, th.angle3, th.vertex2), \
                          (th.angle2, th.angle3, th.vertex1)]
            for a1, a2, v in permutaton:
                a1_cond = indexer.index_value_condition(a1, 'angle')
                a2_cond = indexer.index_value_condition(a2, 'angle')
                if a1_cond.attr_value is None or a2_cond.attr_value is None:
                    continue
                if a1_cond.attr_value == a2_cond.attr_value:
                    it = IsIsoscelesTriangle(th.id, th, v)
                    it_cond = RelationshipBased(it)
                    ret.append([[a1_cond, a2_cond], it_cond])
                    break
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        # Don't need to deduct.
        return sources, target

