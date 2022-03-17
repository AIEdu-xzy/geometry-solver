from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import IsIsoscelesTriangle
from geometry_solver.entity import Triangle
from geometry_solver.common.index_helper import index_equivalent_value


class IsoscelesTriangleJudgment4(Theorem):

    name = "isosceles triangle judgment 4"

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
                eq_cond = index_equivalent_value(indexer,
                        obj1=s1, attr1='length',
                        obj2=s2, attr2='length')
                if eq_cond is not None:
                    it = IsIsoscelesTriangle(th.id, th, v)
                    it_cond = RelationshipBased(it)
                    ret.append([[eq_cond], it_cond])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        # Don't need to deduct.
        return sources, target

