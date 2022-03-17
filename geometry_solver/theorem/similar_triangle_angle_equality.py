from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import SimilarTriangle
from geometry_solver.entity import Triangle


class SimilarTriangleAngleEquality(Theorem):

    name = "similar triangle angle equality"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        st_conds = indexer.index_by_type(SimilarTriangle)
        for cond in st_conds:
            r = cond.relationship
            for angle1, angle2 in r.cor_angle:
                a1_cond = indexer.index_value_condition(angle1, 'angle')
                a2_cond = indexer.index_value_condition(angle2, 'angle')
                if a1_cond.attr_value is None \
                        and a2_cond.attr_value is not None:
                    ret.append([[cond, a2_cond], a1_cond])
                elif a1_cond.attr_value is not None \
                        and a2_cond.attr_value is None:
                    ret.append([[cond, a1_cond], a2_cond])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = sources[1].attr_value
        return sources, target

