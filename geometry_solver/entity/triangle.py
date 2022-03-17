from typing import List
import copy

from geometry_solver.entity.area import Area
from geometry_solver.entity.point import Point
from geometry_solver.entity.line import Line
from geometry_solver.entity.angle import Angle


class Triangle(Area):

    def __init__(self, 
            id_, 
            vertex1: Point,
            vertex2: Point,
            vertex3: Point,
            side1: Line,
            side2: Line,
            side3: Line,
            angle1: Angle,
            angle2: Angle,
            angle3: Angle):
        super(Triangle, self).__init__(
            id_, 
            [vertex1, vertex2, vertex3], 
            [side1, side2, side3], 
            [angle1, angle2, angle3])
        
    @property
    def angle1(self):
        return self.angles[0]
    
    @property
    def angle2(self):
        return self.angles[1]
    
    @property
    def angle3(self):
        return self.angles[2]
    
    @property
    def side1(self):
        return self.sides[0]
    
    @property
    def side2(self):
        return self.sides[1]
    
    @property
    def side3(self):
        return self.sides[2]
    
    @property
    def vertex1(self):
        return self.vertexes[0]
    
    @property
    def vertex2(self):
        return self.vertexes[1]
    
    @property
    def vertex3(self):
        return self.vertexes[2]
    
    @property
    def known_angles(self) -> List[Angle]:
        return [angle for angle in self.angles if angle.angle is not None]

    @property
    def unknown_angles(self) -> List[Angle]:
        return [angle for angle in self.angles if angle.angle is None]

    @property
    def known_sides(self) -> List[Line]:
        return [side for side in self.sides if side.length is not None]
    
    @property
    def unknown_sides(self) -> List[Line]:
        return [side for side in self.sides if side.length is None]

    def opposite_side(self, angle: Angle) -> Line:
        try:
            index = self.angles.index(angle)
        except:
            print('Error: Angle {} is not in triangle!'.format(angle.id))
        return self.sides[index]

    def adjacent_sides(self, angle: Angle) -> List[Line]:
        opposite_side = self.opposite_side(angle)
        return [side for side in self.sides if side is not opposite_side]

    def opposite_angle(self, side: Line) -> Angle:
        try:
            index = self.sides.index(side)
        except:
            print('Error: Side {} is not in triangle!'.format(side.id))
        return self.angles[index]

    def adjacent_angles(self, side: Line) -> List[Angle]:
        opposite_angle = self.opposite_angle(side)
        return [angle for angle in self.angles if angle is not opposite_angle]
    
    def to_rt(self, vertex=None):
        if vertex is None:
            print('Warning: the triangle is not right triangle.')
        self.state.to_rt()

    def to_isosceles(self, vertex=None):
        if vertex is None:
            print('Warning: the triangle is not isosceles.')
        self.to_isosceles(vertex)

    def to_equilateral(self):
        self.to_equilateral()

    def __str__(self) -> str:
        return 'Triangle {}'.format(self.id)

    __repr__ = __str__
