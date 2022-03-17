from typing import List
import math

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState


class LawOfSine(Theorem):

    name = "law of sine"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        pattern = TrianglePattern(
            angle_A=AttributeState.KNOWN,
            angle_B=AttributeState.KNOWN,
            line_BC=AttributeState.KNOWN,
            line_AC=AttributeState.UNKNOWN,
        )
        
        repleced_patterns = indexer.index_by_pattern(pattern)
        return [([p.angle_A, p.angle_B, p.line_BC], p.line_AC) \
                for p in repleced_patterns]

    def deduct(self, sources: List[Condition], target: Condition):
        A = math.radians(sources[0].attr_value)
        B = math.radians(sources[1].attr_value)
        a = sources[2].attr_value
        target.attr_value = a * math.sin(B) / math.sin(A)
        return sources, target

