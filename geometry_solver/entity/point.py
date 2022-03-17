from geometry_solver.entity.entity import Entity


class Point(Entity):

    def __init__(self, id_: str):
        super(Point, self).__init__(id_)
    
    def __str__(self):
        return 'Point {}'.format(self.id)
    
    __repr__ = __str__

