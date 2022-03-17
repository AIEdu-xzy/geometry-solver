from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import IsIsoscelesTriangle
from geometry_solver.entity import Triangle


class IsoscelesTriangleBaseAngleEquality(Theorem):
    
    name = "isosceles triangle's base angle equality"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        i_conds = indexer.index_by_type(IsIsoscelesTriangle)
        
        for cond in i_conds:
            r = cond.relationship
            base_angle = r.base_angle
            a0_cond = indexer.index_value_condition(base_angle[0], 'angle')
            a1_cond = indexer.index_value_condition(base_angle[1], 'angle')
            if a0_cond.attr_value is None \
                    and a1_cond.attr_value is not None:
                ret.append([[cond, a1_cond], a0_cond])
            elif a0_cond.attr_value is not None \
                    and a1_cond.attr_value is None:
                ret.append([[cond, a0_cond], a1_cond])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = sources[1].attr_value
        return sources, target

