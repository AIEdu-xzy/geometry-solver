from typing import List

from geometry_solver.entity.entity import Entity
from geometry_solver.entity.point import Point
from geometry_solver.entity.line import Line
from geometry_solver.entity.angle import Angle


class Area(Entity):

    def __init__(self,
                 id_,
                 vertexes: List[Point], 
                 sides: List[Line], 
                 angles: List[Angle]):
        super(Area, self).__init__(id_)
        self.vertexes = vertexes
        self.sides = sides
        self.angles = angles
        children = vertexes + sides + angles
        self.add_entity(*children)

