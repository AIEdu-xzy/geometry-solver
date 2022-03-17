from typing import List

from geometry_solver.entity.point import Point
from geometry_solver.entity.line import Line
from geometry_solver.relationship import Relationship


class Perpendicular(Relationship):

    def __init__(self, id_: str, line1: Line, line2: Line, foot_point: Point=None):
        """`foot_point can be None. 
        If None, program are responsible to set foot point to lines' intersection`"""
        super(Perpendicular, self).__init__(id_)
        self.line1 = line1
        self.line2 = line2
        self.foot_point = foot_point
    
    def __str__(self):
        return 'Perpendicular({}, {})'.format(
                self.line1.id, self.line2.id)

