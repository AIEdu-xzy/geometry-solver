from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test94():
    link(A, B)
    link(A, D)
    link(C, D)
    link(B, C)
    link(B, O, P, D)
    link(A, P, C)
    link(A, O)

    is_equilateral_triangle('ABC')
    set_length('OD', 1)
    set_length('OA', 1)
    set_angle('AOB', 120)
    common_vertex_angles('A', ['B', 'O', 'C', 'D'])
    common_vertex_angles('B', ['A', 'D', 'C'])
    common_vertex_angles('C', ['D', 'A', 'B'])
    common_vertex_angles('D', ['A', 'B', 'C'])
    set_angle('ADC', 120)
    
    get_angle('BDC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test94()
