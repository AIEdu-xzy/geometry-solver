from typing import List

from geometry_solver.entity.triangle import Triangle
from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import TwoSum


class TriangleAngleSum4(Theorem):
    """已知两角和，推第三角"""

    name = "triangle's angle sum 4"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        triangles = indexer.index_by_type(Triangle)
        exist_relations = {}
        two_sums = indexer.index_by_type(TwoSum)
        for two_sum in two_sums:
            exist_relations[two_sum.relationship.id] = two_sum
        for tri in triangles:
            for angle in tri.angles:
                angle_A_cond = indexer.index_value_condition(angle, 'angle')
                if angle_A_cond.attr_value is None:
                    angle_B, angle_C = [a for a in tri.angles if a != angle]
                    id_ = f'{angle_B.id}.angle_{angle_C.id}.angle'
                    if id_ in exist_relations:
                        two_angle_sum = exist_relations[id_]
                        ret.append([[two_angle_sum], angle_A_cond])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = 180 - sources[0].relationship.sum_value
        return sources, target

