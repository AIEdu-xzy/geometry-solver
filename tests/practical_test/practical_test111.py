from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test111():
    link(A, B)
    link(A, C)
    link(A, D)
    link(B, D, C)
    
    set_angle('BAC', 90)
    is_equilateral_triangle('ABD')
    set_length('AB', 5)
    common_vertex_angles('A', ['B', 'D', 'C'])
    
    get_length('BC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test111()
