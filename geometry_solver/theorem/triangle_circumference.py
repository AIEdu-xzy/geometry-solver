from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, AttributeValue
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.entity import Triangle


class TriangleCircumference(Theorem):

    name = "triangle's circumference"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        triangles = indexer.index_by_type(Triangle)
        for th in triangles:
            side1 = indexer.index_value_condition(th.side1, 'length')
            if side1.attr_value is None: 
                continue
            side2 = indexer.index_value_condition(th.side2, 'length')
            if side2.attr_value is None: 
                continue
            side3 = indexer.index_value_condition(th.side3, 'length')
            if side3.attr_value is None: 
                continue
            ret.append([[side1, side2, side3], 
                        AttributeValue(th, **{'circumference': None})])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = sources[0].attr_value \
                            + sources[1].attr_value \
                            + sources[2].attr_value
        return sources, target

