from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import IsEquilateralTriangle
from geometry_solver.entity import Triangle


class EquilateralTriangleSidesEquality(Theorem):

    name = "equilateral triangle's sides equality"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        e_conds = indexer.index_by_type(IsEquilateralTriangle)
        for cond in e_conds:
            r = cond.relationship
            pre = []
            tg = []
            for side in r.triangle.sides:
                side_cond = indexer.index_value_condition(side, 'length')
                if side_cond.attr_value is None:
                    tg.append(side_cond)
                else:
                    pre.append(side_cond)    
            if pre:
                pre = [cond] + pre
                for t in tg:
                    ret.append([pre, t])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = sources[1].attr_value
        return sources, target

