from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import IsEquilateralTriangle
from geometry_solver.entity import Triangle


class EquilateralTriangleJudgment1(Theorem):

    name = 'equilateral triangle judgement1'

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        e_conds = indexer.index_by_type(IsEquilateralTriangle)
        triangles = indexer.index_by_type(Triangle)
        e_triangles = [cond.relationship.triangle for cond in e_conds]

        def f(th):
            for i in range(3):
                a_cond = indexer.index_value_condition(th.angles[i], 'angle')
                if a_cond.attr_value is None or a_cond.attr_value != 60:
                    yield False
                else:
                    yield True

        for th in triangles:
            if th in e_triangles:
                continue
            if all(f(th)):
                pre = [indexer.index_value_condition(th.angles[i], 'angle') \
                         for i in range(3)]
                r = IsEquilateralTriangle(th.id, th)
                tg = RelationshipBased(r)
                ret.append([pre, tg])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        # Don't need to deduct.
        return sources, target

