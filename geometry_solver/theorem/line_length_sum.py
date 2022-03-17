from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition, RelationshipBased
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import Collineation


class LineLengthSum(Theorem):

    name = "line length sum"

    def __init__(self):
        super(LineLengthSum, self).__init__()

    def _find_lines_by_collineation(self, 
            col_cond: RelationshipBased, 
            indexer: Indexer):
        col = col_cond.relationship
        ps = col.points
        size = len(ps)
        # Find line sum permutation.
        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    line_ij = indexer.index_line_by_points(ps[i], ps[j])
                    line_jk = indexer.index_line_by_points(ps[j], ps[k])
                    line_ik = indexer.index_line_by_points(ps[i], ps[k])
                    cond_ij = indexer.index_value_condition(line_ij, 'length')
                    cond_jk = indexer.index_value_condition(line_jk, 'length')
                    cond_ik = indexer.index_value_condition(line_ik, 'length')
                    if sum([cond_ij.attr_value == None, 
                            cond_jk.attr_value == None, 
                            cond_ik.attr_value == None]) == 1:
                        return [[col_cond, cond_ij, cond_jk], (cond_ik)]
        return None

    def index(self, indexer: Indexer):
        conditions = []
        cols = indexer.index_by_type(Collineation)
        for col_cond in cols:
            cond = self._find_lines_by_collineation(col_cond, indexer)
            if cond is not None:
                conditions.append(cond)
        return conditions

    def deduct(self, sources: List[Condition], target: Condition):
        """sources and target here are difference from regular theorem.
        
        Let A, B, C collineation. Then AB + BC = AC.
        So [AB, BC] are sources, AC is target.
        During deduction, target will be modified as the condition whose 
            attr_value is none.
        """
        AB = sources[1]
        BC = sources[2]
        AC = target
        if AC.attr_value is None:
            AC.attr_value = AB.attr_value + BC.attr_value
            sources[1:] = [AB, BC]
            target = AC
        elif AB.attr_value is None:
            AB.attr_value = AC.attr_value - BC.attr_value
            sources[1:] = [AC, BC]
            target = AB
        else:
            BC.attr_value = AC.attr_value - AB.attr_value
            sources[1:] = [AC, AB]
            target = BC
        return sources, target

