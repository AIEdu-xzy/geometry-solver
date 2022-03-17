from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test109():
    link(A, B)
    link(A, E, C)
    link(A, O, D)
    link(B, D, C)
    link(B, O, E)
    
    perpendicular('AD', 'BC')
    split_angle('ABC', 'BE')
    set_angle('ABC', 64)
    set_angle('AEB', 70)
    common_vertex_angles('A', ['B', 'D', 'C'])
    common_vertex_angles('B', ['A', 'E', 'C'])
    
    get_angle('CAD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test109()
