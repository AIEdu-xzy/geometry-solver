from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import IsIsoscelesTriangle
from geometry_solver.entity import Triangle


class IsoscelesTriangleHypotenuseEquality(Theorem):
    
    name = "isosceles triangle's hypotenuse equality"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        i_conds = indexer.index_by_type(IsIsoscelesTriangle)
        
        for cond in i_conds:
            r = cond.relationship
            h = r.hypotenuse
            h0_cond = indexer.index_value_condition(h[0], 'length')
            h1_cond = indexer.index_value_condition(h[1], 'length')
            if h0_cond.attr_value is None \
                    and h1_cond.attr_value is not None:
                ret.append([[cond, h1_cond], h0_cond])
            elif h0_cond.attr_value is not None \
                    and h1_cond.attr_value is None:
                ret.append([[cond, h0_cond], h1_cond])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = sources[1].attr_value
        return sources, target

