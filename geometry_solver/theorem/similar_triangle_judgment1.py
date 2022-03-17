from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import SimilarTriangle
from geometry_solver.entity import Triangle


class SimilarTriangleJudgment1(Theorem):

    name = "similar triangle judgment 1"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        triangles = indexer.index_by_type(Triangle)
        pattern = TrianglePattern(angle_A=AttributeState.KNOWN,
                                  angle_B=AttributeState.KNOWN,
                                  angle_C=AttributeState.KNOWN)
        
        st_conds = indexer.index_by_type(SimilarTriangle)
        all_st = [cond.relationship for cond in st_conds]
        
        def get_corresp():
            th1_conds = [indexer.index_value_condition(th1_angle, 'angle') \
                    for th1_angle in th1.angles]
            th2_conds = [indexer.index_value_condition(th2_angle, 'angle') \
                    for th2_angle in th2.angles]
            cor_angle = []
            for cond1 in th1_conds:
                for cond2 in th2_conds:
                    if cond1.attr_value == cond2.attr_value:
                        cor_angle.append((cond1.obj, cond2.obj))
                        break
            return cor_angle, th1_conds, th2_conds
        
        replaced, entities = indexer.index_by_pattern(pattern, True)
        size = len(entities)
        for i in range(size):
            for j in range(i + 1, size):
                i_angles = set([replaced[i].angle_A, 
                                replaced[i].angle_B, 
                                replaced[i].angle_C])
                j_angles = set([replaced[j].angle_A, 
                                replaced[j].angle_B, 
                                replaced[j].angle_C])
                if i_angles == j_angles:
                    th1 = entities[i]
                    th2 = entities[j]
                    cor_angle, conds1, conds2 = get_corresp()
                    st = SimilarTriangle('_'.join([th1.id, th2.id]),
                                    th1, th2, cor_angle)
                    if st not in all_st:
                        ret.append([conds1+conds2, RelationshipBased(st)])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        # Don't need to deduct.
        return sources, target

