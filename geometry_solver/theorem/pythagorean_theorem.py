from typing import List
import math

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, AttributeValue
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.entity import Triangle
from geometry_solver.relationship import IsRightTriangle
from geometry_solver.common.utils import attr_value_known_num


class PythagoreanTheorem(Theorem):

    name = "pythagorean theorem"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        rt_conds = indexer.index_by_type(IsRightTriangle)
        for cond in rt_conds:
            r = cond.relationship
            hypotenuse = r.hypotenuse
            legs = r.legs
            a = indexer.index_value_condition(legs[0], 'length')
            b = indexer.index_value_condition(legs[1], 'length')
            c = indexer.index_value_condition(hypotenuse, 'length')
            if attr_value_known_num([a, b, c]) == 2:
                ret.append([[cond, a, b], c])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        a = sources[1].attr_value
        b = sources[2].attr_value
        c = target.attr_value
        if a is None:
            a = math.sqrt(c*c - b*b)
            sources[1], sources[2], target = sources[2], target, sources[1]
            target.attr_value = a
        elif b is None:
            b = math.sqrt(c*c - a*a)
            sources[1], sources[2], target = sources[1], target, sources[2]
            target.attr_value = b
        else:
            target.attr_value = math.sqrt(a*a + b*b)
        return sources, target

