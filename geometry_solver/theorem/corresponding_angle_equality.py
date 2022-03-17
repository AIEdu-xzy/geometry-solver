from typing import List

from geometry_solver.theorem.theorem import Theorem
from geometry_solver.condition import Condition
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.pattern import TrianglePattern, AttributeState
from geometry_solver.relationship import Parallel


class CorrespondingAngleEquality(Theorem):

    name = 'corresponding angle equality'

    def __init__(self):
        super().__init__()
    
    def index(self, indexer: Indexer):
        """Find corresponding angles from parallel relationship."""
        ret = []


        def find_corresponding_angles(link_col, col1, col2, p1, p2):
            for i in [0, -1]:
                for j in [0, -1]:
                    if link_col[i] == p1 or col1[j] == p1:
                        continue
                    if link_col[i] == p2 or col2[j] == p2:
                        continue
                    angle1 = indexer.index_angle_by_points(\
                        link_col[i], p1, col1[j])
                    angle2 = indexer.index_angle_by_points(\
                        link_col[i], p2, col2[j])
                    a1_cond = indexer.index_value_condition(angle1, 'angle')
                    a2_cond = indexer.index_value_condition(angle2, 'angle')
                    if a1_cond.attr_value is None \
                            and a2_cond.attr_value is not None:
                        ret.append([[a2_cond], a1_cond])
                    elif a1_cond.attr_value is not None \
                            and a2_cond.attr_value is None:
                        ret.append([[a1_cond], a2_cond])


        conds = indexer.index_by_type(Parallel)
        for cond in conds:
            r = cond.relationship
            line1, line2 = r.line1, r.line2
            # col is a list of point entity.
            col1 = indexer.index_collineation_by_line(line1)
            col2 = indexer.index_collineation_by_line(line2)
            if r.reverse:
                col2 = list(reversed(col2))
            for p1 in col1:
                for p2 in col2:
                    # Link line is the line links two parallel lines.
                    link_line = indexer.index_line_by_points(p1, p2)
                    # One link line can generate four corresponding angles at most.
                    if link_line is None:
                        continue
                    link_col = indexer.index_collineation_by_line(link_line)
                    find_corresponding_angles(link_col, col1, col2, p1, p2)
                    
        return ret

    def deduct(self, sources: List[Condition], target: Condition):
        target.attr_value = sources[0].attr_value
        return sources, target

