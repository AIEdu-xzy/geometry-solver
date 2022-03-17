from geometry_solver.relationship.relationship import Relationship


class IsRightTriangle(Relationship):
    
    def __init__(self, id_, triangle, right_angle):
        super().__init__(id_)
        self.triangle = triangle
        self.right_angle = right_angle
        
    @property
    def legs(self):
        rt_index = self.triangle.angles.index(self.right_angle)
        legs_index = [i for i in range(3) if i != rt_index]
        legs = [self.triangle.sides[i] for i in legs_index]
        return legs
    
    @property
    def hypotenuse(self):
        rt_index = self.triangle.angles.index(self.right_angle)
        return self.triangle.sides[rt_index]
    
    def __str__(self):
        return 'Right triangle({})'.format(self.triangle.id)

