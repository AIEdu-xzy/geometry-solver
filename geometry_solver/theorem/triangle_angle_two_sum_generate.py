from typing import List
import itertools

from geometry_solver.entity.triangle import Triangle
from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import TwoSum


class TriangleTwoSumGenerate(Theorem):
    """三角形内部的角度生成TwoSum对象"""

    name = "triangle angle two sum generate"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        triangles = indexer.index_by_type(Triangle)
        exist_relations = set()
        two_sums = indexer.index_by_type(TwoSum)
        for two_sum in two_sums:
            exist_relations.add(two_sum.relationship.id)
        for tri in triangles:
            known_angles = []
            for angle in tri.angles:
                angle_A_cond = indexer.index_value_condition(angle, 'angle')
                if angle_A_cond.attr_value is not None:
                    known_angles.append(angle_A_cond)
            
            if len(known_angles) >= 2:
                pairs = itertools.product(known_angles, known_angles)
                for angle_B_cond, angle_C_cond in pairs:
                    id_ = f'{angle_B_cond.obj.id}.angle_{angle_C_cond.obj.id}.angle'
                    if id_ in exist_relations:
                        continue
                    two_sum_relation = TwoSum(id_,
                            angle_B_cond.obj, 'angle',
                            angle_C_cond.obj, 'angle',
                            angle_B_cond.attr_value + angle_C_cond.attr_value)
                    r = RelationshipBased(two_sum_relation)
                    ret.append([[angle_B_cond, angle_C_cond], r])

        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        return sources, target


