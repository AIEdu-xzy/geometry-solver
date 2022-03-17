from geometry_solver.relationship.is_isosceles_triangle import IsIsoscelesTriangle


class IsEquilateralTriangle(IsIsoscelesTriangle):
    
    def __init__(self, id_, triangle):
        super().__init__(id_, triangle, triangle.vertex1)
    
    def __str__(self):
        return 'Equilateral triangle({})'.format(self.triangle.id)

