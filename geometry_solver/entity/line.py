from typing import List

from geometry_solver.entity.entity import Entity
from geometry_solver.entity.point import Point


class Line(Entity):

    def __init__(self, id_: str, end1: Point, end2: Point):
        super(Line, self).__init__(id_)
        self.end1 = end1
        self.end2 = end2
        self.add_entity(end1, end2)

    def __str__(self):
        return 'Line {}'.format(self.id)

