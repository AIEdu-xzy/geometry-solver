from typing import List

from geometry_solver.entity.triangle import Triangle
from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import TwoSum


class TriangleAngleSum3(Theorem):
    """已知一角，推两角和"""

    name = "triangle's angle sum 3"

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
            for angle in tri.angles:
                angle_A_cond = indexer.index_value_condition(angle, 'angle')
                if angle_A_cond.attr_value is not None:
                    angle_B, angle_C = [a for a in tri.angles if a != angle]
                    id_ = f'{angle_B.id}.angle_{angle_C.id}.angle'
                    if id_ in exist_relations:
                        continue
                    two_sum_relation = TwoSum(id_,
                            angle_B, 'angle',
                            angle_C, 'angle',
                            180 - angle_A_cond.attr_value)
                    r = RelationshipBased(two_sum_relation)
                    ret.append([[angle_A_cond], r])

        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        return sources, target

