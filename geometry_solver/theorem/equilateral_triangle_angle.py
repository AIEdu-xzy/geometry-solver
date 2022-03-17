from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import IsEquilateralTriangle
from geometry_solver.entity import Triangle


class EquilateralTriangleAngle(Theorem):

    name = "equilateral triangle's angle equals to 60 degree."

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        e_conds = indexer.index_by_type(IsEquilateralTriangle)
        for cond in e_conds:
            r = cond.relationship
            tg = []
            for angle in r.triangle.angles:
                angle_cond = indexer.index_value_condition(angle, 'angle')
                if angle_cond.attr_value is None:
                    tg.append(angle_cond)
            for t in tg:
                ret.append([[cond], t])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = 60
        return sources, target

