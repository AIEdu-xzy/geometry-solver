from typing import List

from geometry_solver.relationship.relationship import Relationship
from geometry_solver.entity import Point, Angle, Line


class NAngleSector(Relationship):

    def __init__(self, id_: str, angle: Angle, split_line: Line, near_line=None):
        super().__init__(id_)
        self.angle = angle
        self.split_line = split_line
        self.near_line = near_line
        if near_line is None:
            self.near_line = angle.side1
            
    @property
    def far_line(self):
        if self.near_line == self.angle.side1:
            line = self.angle.side2
        else:
            line = self.angle.side1
        return line
    
    @property
    def three_ends(self):
        near_line = self.near_line
        split_line = self.split_line
        far_line = self.far_line
        vertex = self.angle.vertex
        
        def another_end(line, end):
            return line.end1 if end == line.end2 else line.end2
        
        p_near = another_end(near_line, vertex)
        p_split = another_end(split_line, vertex)
        p_far = another_end(far_line, vertex)
        return [p_near, p_split, p_far]

    @property
    def vertex(self):
        return self.angle.vertex

    def __str__(self):
        return 'NAngleSector({}, {})'.format(
                self.angle.id, self.split_line.id)

