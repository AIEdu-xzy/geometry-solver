from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import NAngleSector
from geometry_solver.entity import Triangle
from geometry_solver.common.utils import attr_value_known_num


class NAngleSectorProportional(Theorem):

    name = "n angle sector proportional"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        
        nas_conds = indexer.index_by_type(NAngleSector)
        for cond in nas_conds:
            r = cond.relationship
            # Existence of ratio condition is guaranteed.
            ratio_cond = indexer.index_value_condition(r, 'ratio')
            ratio = ratio_cond.attr_value
            p_near, p_split, p_far = r.three_ends
            vertex = r.vertex
            angle_near = indexer.index_angle_by_points(p_near, vertex, p_split)
            angle_far = indexer.index_angle_by_points(p_far, vertex, p_split)
            angle_full = indexer.index_angle_by_points(p_near, vertex, p_far)
            
            near_cond = indexer.index_value_condition(angle_near, 'angle')
            far_cond = indexer.index_value_condition(angle_far, 'angle')
            full_cond = indexer.index_value_condition(angle_full, 'angle')
            
            if full_cond.attr_value is None:
                if near_cond.attr_value is not None:
                    ret.append([[near_cond, ratio_cond, 1/ratio], full_cond])
                elif far_cond.attr_value is not None:
                    ret.append([[far_cond, ratio_cond, 1/(1-ratio)], full_cond])
            if near_cond.attr_value is None:
                if full_cond.attr_value is not None:
                    ret.append([[full_cond, ratio_cond, ratio], near_cond])
                elif far_cond.attr_value is not None:
                    ret.append([[far_cond, ratio_cond, ratio/(1-ratio)], near_cond])
            if far_cond.attr_value is None:
                if full_cond.attr_value is not None:
                    ret.append([[full_cond, ratio_cond, 1-ratio], far_cond])
                elif near_cond.attr_value is not None:
                    ret.append([[near_cond, ratio_cond, (1-ratio)/ratio], far_cond])
            
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        ratio = sources[-1]
        target.attr_value = sources[0].attr_value * ratio
        return sources[:-1], target

