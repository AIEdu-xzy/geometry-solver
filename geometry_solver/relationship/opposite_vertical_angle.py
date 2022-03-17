from typing import List

from geometry_solver.entity.angle import Angle
from geometry_solver.entity.point import Point
from geometry_solver.relationship import Relationship


class OppositeVerticalAngle(Relationship):

    def __init__(self, id_: str, angle1: Angle, angle2: Angle, vertex: Point):
        super(OppositeVerticalAngle, self).__init__(id_)
        self.angle1 = angle1
        self.angle2 = angle2
        self.vertex = vertex
    
    def __str__(self):
        return 'VerticalAngle({}, {})'.format(
                self.angle1.id ,self.angle2.id)

