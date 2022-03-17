from typing import List

from geometry_solver.entity.point import Point
from geometry_solver.entity.line import Line
from geometry_solver.relationship import Relationship


class CommonVertexAngle(Relationship):

    def __init__(self, id_: str, vertex: Point, ends: List[Point]):
        super(CommonVertexAngle, self).__init__(id_)
        self.vertex = vertex
        self.ends = ends
    
    def __str__(self):
        return 'CommonVertexAngle({}, {})'.format(
                self.vertex.id, ''.join([p.id for p in self.ends]))

