from typing import List

from geometry_solver.entity.angle import Angle
from geometry_solver.relationship import Relationship


class SupplementaryAngle(Relationship):

    def __init__(self, id_: str,  angle1: Angle, angle2: Angle):
        super(SupplementaryAngle, self).__init__(id_)
        self.angle1 = angle1
        self.angle2 = angle2
    
    def __str__(self):
        return 'Supplementary({}, {})'.format(
                self.angle1.id, self.angle2.id)

