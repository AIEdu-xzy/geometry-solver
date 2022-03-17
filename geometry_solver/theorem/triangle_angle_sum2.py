from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.common.index_helper import index_equivalent_value


class TriangleAngleSum2(Theorem):
    """已知一角，且剩余两角相等"""

    name = "triangle's angle sum 2"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        pattern = TrianglePattern(
            angle_A=AttributeState.KNOWN,
            angle_B=AttributeState.UNKNOWN,
            angle_C=AttributeState.UNKNOWN
        )
        repleced_patterns = indexer.index_by_pattern(pattern)
        for p in repleced_patterns:
            angle1 = p.angle_B.obj
            angle2 = p.angle_C.obj
            eq_cond = index_equivalent_value(indexer, angle1, 'angle', angle2, 'angle')
            if eq_cond is not None:
                ret.append([[eq_cond, p.angle_A], [p.angle_B, p.angle_C]])
        return ret

    def deduct(self, sources: List[Condition], target: List[Condition]):
        rest = 180 - sources[1].attr_value
        target[0].attr_value = rest / 2
        target[1].attr_value = rest - target[0].attr_value
        return sources, target

