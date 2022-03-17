from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import CommonVertexAngle
from geometry_solver.common.index_helper import index_equivalent_value
from geometry_solver.common.utils import attr_value_known_num


class CommonVertexAngleSum2(Theorem):

    name = 'common-vertex angle sum 2'

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
                    cond_ik = indexer.index_value_condition(angle_ik, 'angle')
                    if cond_ik.attr_value is None:
                        continue
                    eq_cond = index_equivalent_value(
                            indexer, angle_ij, 'angle', angle_jk, 'angle')
                    if eq_cond is None:
                        continue
                    cond_ij = indexer.index_value_condition(angle_ij, 'angle')
                    cond_jk = indexer.index_value_condition(angle_jk, 'angle')
                    unkown_cond = [c for c in [cond_ij, cond_jk] if c.attr_value is None]
                    if not unkown_cond:
                        continue
                    return [[eq_cond, cond_ik], unkown_cond]
        return None
    
    def index(self, indexer: Indexer):
        conditions = []
        cvas = indexer.index_by_type(CommonVertexAngle)
        for cva_cond in cvas:
            cond = self._find_common_vertex_angle(cva_cond, indexer)
            if cond is not None:
                conditions.append(cond)
        return conditions

    def deduct(self, sources: List[Condition], target: List[Condition]):
        half = sources[1].attr_value / 2
        for tg in target:
            tg.attr_value = half
        return sources, target

