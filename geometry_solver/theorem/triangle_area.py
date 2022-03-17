from typing import List
import math

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, AttributeValue
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.entity import Triangle


class TriangleArea(Theorem):

    name = "triangle area"

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
            area = indexer.index_value_condition(th, 'area')
            if area.attr_value is None:
                ret.append([[side1, side2, side3], area])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        a = sources[0].attr_value
        b = sources[1].attr_value
        c = sources[2].attr_value
        p = (a + b + c) / 2
        target.attr_value = math.sqrt(p * (p-a) * (p-b) * (p-c))
        return sources, target

