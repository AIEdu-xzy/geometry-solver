from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test82():
    link(A, B)
    link(A, C)
    link(A, E, D)
    link(B, D, C)
    link(B, E)
    link(C, E)

    is_equilateral_triangle('ABC')
    perpendicular('AD', 'BC')
    set_angle('EBC', 45)
    common_vertex_angles('B', ['A', 'E', 'C'])
    common_vertex_angles('C', ['A', 'E', 'B'])
    common_vertex_angles('A', ['B', 'D', 'C'])
    
    get_angle('BAE')

    return get_problem()
    

if __name__ == '__main__':
    practical_test82()
