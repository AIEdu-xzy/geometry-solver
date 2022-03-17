from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import SupplementaryAngle
from geometry_solver.relationship import TwoSum


class SupplementaryAngleSum2(Theorem):

    name = "supplementary angle sum 2"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        conds = indexer.index_by_type(SupplementaryAngle)
        exist_relations = set()
        two_sums = indexer.index_by_type(TwoSum)
        for two_sum in two_sums:
            exist_relations.add(two_sum.relationship.id)
        for cond in conds:
            r = cond.relationship
            angle1_cond = indexer.index_value_condition(r.angle1, 'angle')
            angle2_cond = indexer.index_value_condition(r.angle2, 'angle')
            id_ = f'{angle1_cond.obj.id}.angle_{angle2_cond.obj.id}.angle'
            if id_ in exist_relations:
                continue
            two_sum_relation = TwoSum(id_,
                    angle1_cond.obj, 'angle',
                    angle2_cond.obj, 'angle',
                    180)
            r = RelationshipBased(two_sum_relation)
            ret.append([[cond], r])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        return sources, target

