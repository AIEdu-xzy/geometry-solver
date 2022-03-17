from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test96():
    link(A, B)
    link(A, C)
    link(B, D, C)
    link(A, E, D)
    link(B, E)
    link(C, E)

    perpendicular('AD', 'BC')
    set_angle('EBC', 45)
    is_equilateral_triangle('ABC')
    common_vertex_angles('A', ['B', 'D', 'C'])
    common_vertex_angles('B', ['A', 'E', 'C'])
    common_vertex_angles('C', ['A', 'E', 'B'])
    
    get_angle('BED')

    return get_problem()
    

if __name__ == '__main__':
    practical_test96()
