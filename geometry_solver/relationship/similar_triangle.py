from typing import List, Tuple

from geometry_solver.entity.triangle import Triangle
from geometry_solver.entity.angle import Angle
from geometry_solver.relationship import Relationship


class SimilarTriangle(Relationship):

    def __init__(self, 
                 id_: str, 
                 triangle1: Triangle, 
                 triangle2: Triangle, 
                 cor_angle: List[Tuple[Angle, Angle]]):
        super().__init__(id_)
        self.triangle1 = triangle1
        self.triangle2 = triangle2
        # Similar triangles' corresponding angles.
        self.cor_angle = cor_angle
        
        # Similar triangles' corresponding sides.
        self.cor_sides = []
        for angle1, angle2 in cor_angle:
            side1 = (triangle1.opposite_side(angle1))
            side2 = (triangle2.opposite_side(angle2))
            self.cor_sides.append((side1, side2))
    
    def __eq__(self, other):
        if not isinstance(other, SimilarTriangle):
            return False
        return \
            ( \
                self.triangle1 == other.triangle1 \
                and \
                self.triangle2 == other.triangle2 \
            ) \
            or \
            ( \
                self.triangle1 == other.triangle2 \
                and \
                self.triangle2 == other.triangle1 \
            )
    
    def __hash__(self):
        tid1, tid2 = self.triangle1.id, self.triangle2.id
        tid1, tid2 = sorted([tid1, tid2])
        return hash('_'.join(['SimilarTriangle', tid1, tid2]))
    
    def __str__(self):
        return 'SimilarTriangle({}, {})'.format(
                self.triangle1.id, self.triangle2.id)

