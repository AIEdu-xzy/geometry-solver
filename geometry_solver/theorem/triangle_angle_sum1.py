from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState


class TriangleAngleSum1(Theorem):

    name = "triangle's angle sum 1"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        pattern = TrianglePattern(
            angle_A=AttributeState.KNOWN,
            angle_B=AttributeState.KNOWN,
            angle_C=AttributeState.UNKNOWN
        )
        # After index pattern.angle_A and pattern.angle_B are 
        # replaced by AttributeValue condition, and angle_C is
        # also replaced by AttributeValue condition whose value
        # is unkonwn.
        repleced_patterns = indexer.index_by_pattern(pattern)
        return [([p.angle_A, p.angle_B], p.angle_C) for p in repleced_patterns]

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = 180 \
                            - sources[0].attr_value \
                            - sources[1].attr_value
        return sources, target

