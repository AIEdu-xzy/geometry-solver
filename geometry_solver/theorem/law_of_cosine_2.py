from typing import List
import math

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState


class LawOfCosine2(Theorem):
    
    name = "law of cosine 2"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        pattern = TrianglePattern(
            line_AB=AttributeState.KNOWN,
            line_AC=AttributeState.KNOWN,
            line_BC=AttributeState.KNOWN,
            angle_A=AttributeState.UNKNOWN
        )
        
        repleced_patterns = indexer.index_by_pattern(pattern)
        return [([p.line_AB, p.line_AC, p.line_BC], p.angle_A) \
                for p in repleced_patterns]

    def deduct(self, sources: List[Condition], target: Condition):
        a = sources[0].attr_value
        b = sources[1].attr_value
        c = sources[2].attr_value
        cos_theta = (a**2 + b**2 - c**2) / (2*a*b)
        theta = math.degrees(math.acos(cos_theta))
        target.attr_value = theta
        return sources, target

