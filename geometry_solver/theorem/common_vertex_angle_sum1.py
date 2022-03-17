from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import CommonVertexAngle


class CommonVertexAngleSum1(Theorem):

    name = 'common-vertex angle sum 1'

    def __init__(self):
        super().__init__()
        
    def _find_common_vertex_angle(self, 
            cva_cond: RelationshipBased, 
            indexer: Indexer):
        r = cva_cond.relationship
        vertex = r.vertex
        ends = r.ends
        size = len(ends)
        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    angle_ij = indexer.index_angle_by_points(
                        ends[i], vertex, ends[j])
                    angle_jk = indexer.index_angle_by_points(
                        ends[j], vertex, ends[k])
                    angle_ik = indexer.index_angle_by_points(
                        ends[i], vertex, ends[k])
                    cond_ij = indexer.index_value_condition(angle_ij, 'angle')
                    cond_jk = indexer.index_value_condition(angle_jk, 'angle')
                    cond_ik = indexer.index_value_condition(angle_ik, 'angle')
                    if sum([cond_ij.attr_value is None, 
                            cond_jk.attr_value is None, 
                            cond_ik.attr_value is None]) == 1:
                        return [[cva_cond, cond_ij, cond_jk], (cond_ik)]
        return None
    
    def index(self, indexer: Indexer):
        conditions = []
        cvas = indexer.index_by_type(CommonVertexAngle)
        for cva_cond in cvas:
            cond = self._find_common_vertex_angle(cva_cond, indexer)
            if cond is not None:
                conditions.append(cond)
        return conditions

    def deduct(self, sources: List[Condition], target: Condition):
        BAC = sources[1]
        CAD = sources[2]
        BAD = target
        if BAD.attr_value is None:
            BAD.attr_value = BAC.attr_value + CAD.attr_value
            sources[1:] = [BAC, CAD]
            target = BAD
        elif BAC.attr_value is None:
            BAC.attr_value = BAD.attr_value - CAD.attr_value
            sources[1:] = [BAD, CAD]
            target = BAC
        else:
            CAD.attr_value = BAD.attr_value - BAC.attr_value
            sources[1:] = [BAD, BAC]
            target = CAD
        return sources, target

