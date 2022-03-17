from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased, AttributeValue
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import SimilarTriangle
from geometry_solver.entity import Triangle


class SimilarRatioDetermination(Theorem):

    name = "similar ratio determination of similar triangle"

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        ret = []
        st_conds = indexer.index_by_type(SimilarTriangle)
        
        for cond in st_conds:
            r = cond.relationship
            for side1, side2 in r.cor_sides:
                side1_cond = indexer.index_value_condition(side1, 'length')
                side2_cond = indexer.index_value_condition(side2, 'length')
                if side1_cond.attr_value is not None \
                        and side2_cond.attr_value is not None:
                    ratio = indexer.index_value_condition(r, 'ratio')
                    if ratio.attr_value is None:
                        ret.append([[cond, side1_cond, side2_cond], ratio])
                    break
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        triangle1_line = sources[1].attr_value
        triangle2_line = sources[2].attr_value
        target.attr_value = triangle1_line / triangle2_line
        return sources, target

