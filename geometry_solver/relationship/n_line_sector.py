from typing import List

from geometry_solver.entity.point import Point
from geometry_solver.entity.line import Line
from geometry_solver.relationship import Relationship


class NLineSector(Relationship):

    def __init__(self, id_: str, line: Line, split_point: Point, near_point: Point=None):
        super(NLineSector, self).__init__(id_)
        self.line = line
        self.split_point = split_point
        self.near_point = near_point
        if near_point:
            self.near_point = line.end1
    
    @property
    def far_point(self):
        if self.near_point == self.line.end1:
            point = self.line.end2
        else:
            point = self.line.end1
        return point
    
    @property
    def three_points(self):
        return self.near_point, self.split_point, self.far_point
    
    def __str__(self):
        return 'NLineSector({}, {})'.format(
                self.split_point.id, self.point.id)

