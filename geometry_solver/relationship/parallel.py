from typing import List

from geometry_solver.entity.line import Line
from geometry_solver.relationship import Relationship
from geometry_solver.relationship.collineation import Collineation


class Parallel(Relationship):

    def __init__(self, 
                 id_: str, 
                 line1: Line,
                 line2: Line,
                 reverse=False):
        """param `reverse` indicates the direction of two lines 
        is the same or reversed.
        Direction of line can be determined by `end1` and `end2`.
        """
        super(Parallel, self).__init__(id_)
        self.line1 = line1
        self.line2 = line2
        self.reverse = reverse
    
    def __str__(self):
        return 'Parallel({}, {})'.format(
                self.line1.id, self.line2.id)
