from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import SimilarTriangle
from geometry_solver.entity import Triangle


class SimilarTriangleSidesProportional(Theorem):

    name = "similar triangle sides proportional"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        st_conds = indexer.index_by_type(SimilarTriangle)
        for cond in st_conds:
            r = cond.relationship
            ratio_cond = indexer.index_value_condition(r, 'ratio')
            if ratio_cond.attr_value is None:
                continue
            for side1, side2 in r.cor_sides:
                s1_cond = indexer.index_value_condition(side1, 'length')
                s2_cond = indexer.index_value_condition(side2, 'length')
                if sum([s1_cond.attr_value is None, 
                        s2_cond.attr_value is None]) == 1:
                    ret.append([[cond, s1_cond, ratio_cond], s2_cond])
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        line1 = sources[1]
        line2 = target
        ratio = sources[2].attr_value
        
        if line2.attr_value is None:
            line2.attr_value = line1.attr_value / ratio
            target = line2
            sources[1] = line1
        else:
            line1.attr_value = line2.attr_value * ratio
            target = line1
            sources[1] = line2
        return sources, target

