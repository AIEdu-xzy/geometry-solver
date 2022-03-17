from geometry_solver.relationship.relationship import Relationship


class IsIsoscelesTriangle(Relationship):
    
    def __init__(self, id_, triangle, vertex):
        super().__init__(id_)
        self.triangle = triangle
        self.vertex = vertex
        self._v_index = self.triangle.vertexes.index(vertex)
        self._h_index = [i for i in range(3) if i != self._v_index]
        
    @property
    def base_side(self):
        return self.triangle.sides[self._v_index]
    
    @property
    def hypotenuse(self):
        return [self.triangle.sides[i] for i in self._h_index]
    
    @property
    def apex_angle(self):
        return self.triangle.angles[self._v_index]
    
    @property
    def base_angle(self):
        return [self.triangle.angles[i] for i in self._h_index]
    
    def __str__(self):
        return 'Isosceles triangle({})'.format(self.triangle.id)

