from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import IsIsoscelesTriangle
from geometry_solver.entity import Triangle


class IsoscelesTriangleJudgment2(Theorem):

    name = "isosceles triangle judgment 2"

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
            permutaton = [(th.side1, th.side2, th.vertex3), \
                          (th.side1, th.side3, th.vertex2), \
                          (th.side2, th.side3, th.vertex1)]
            for s1, s2, v in permutaton:
                s1_cond = indexer.index_value_condition(s1, 'length')
                s2_cond = indexer.index_value_condition(s2, 'length')
                if s1_cond.attr_value is None or s2_cond.attr_value is None:
                    continue
                if s1_cond.attr_value == s2_cond.attr_value:
                    it = IsIsoscelesTriangle(th.id, th, v)
                    it_cond = RelationshipBased(it)
                    ret.append([[s1_cond, s2_cond], it_cond])
                    break
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        # Don't need to deduct.
        return sources, target

