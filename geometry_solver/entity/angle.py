from typing import List

from geometry_solver.entity.entity import Entity
from geometry_solver.entity.point import Point
from geometry_solver.entity.line import Line


class Angle(Entity):

    def __init__(self, 
                 id_, 
                 side1: Line, 
                 side2: Line, 
                 vertex: Point):
        super(Angle, self).__init__(id_)
        self.side1 = side1
        self.side2 = side2
        self.vertex = vertex
        self.add_entity(side1, side2, vertex)

    def __str__(self):
        return 'Angle {}'.format(self.id)

