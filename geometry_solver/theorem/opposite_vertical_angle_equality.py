from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import OppositeVerticalAngle


class OppositeVertivalAngleEquality(Theorem):

    name = "opposite vertical angle equality"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        conds = indexer.index_by_type(OppositeVerticalAngle)
        for cond in conds:
            r = cond.relationship
            angle1_cond = indexer.index_value_condition(r.angle1, 'angle')
            angle2_cond = indexer.index_value_condition(r.angle2, 'angle')
            if angle1_cond.attr_value is not None and \
                    angle2_cond.attr_value is None:
                ret.append([[cond, angle1_cond], angle2_cond])
            elif angle1_cond.attr_value is None and \
                    angle2_cond.attr_value is not None:
                ret.append([[cond, angle2_cond], angle1_cond])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = sources[1].attr_value
        return sources, target

