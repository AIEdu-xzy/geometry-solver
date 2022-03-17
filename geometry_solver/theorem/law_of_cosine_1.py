from typing import List
import math

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState


class LawOfCosine1(Theorem):
    
    name = "law of cosine 1"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        pattern = TrianglePattern(
            angle_A=AttributeState.KNOWN,
            line_AB=AttributeState.KNOWN,
            line_AC=AttributeState.KNOWN,
            line_BC=AttributeState.UNKNOWN,
        )
        
        repleced_patterns = indexer.index_by_pattern(pattern)
        return [([p.angle_A, p.line_AB, p.line_AC], p.line_BC) \
                for p in repleced_patterns]

    def deduct(self, sources: List[Condition], target: Condition):
        gama = math.radians(sources[0].attr_value)
        a = sources[1].attr_value
        b = sources[2].attr_value
        target.attr_value = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(gama))
        return sources, target

