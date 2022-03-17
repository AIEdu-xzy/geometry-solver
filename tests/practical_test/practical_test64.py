from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test64():
    link(A, B)
    link(B, C)
    link(A, C)
    link(P, A)
    link(P, B)
    link(P, C)

    set_length('PA', 2)
    set_length('PC', 1)
    set_angle('ACB', 90)
    set_angle('APC', 135)
    line_equivalence('AC', 'BC')
    common_vertex_angles('C', ['A', 'P', 'B'])
    common_vertex_angles('A', ['B', 'P', 'C'])
    common_vertex_angles('B', ['A', 'P', 'C'])
    
    get_length('BP')

    return get_problem()
    

if __name__ == '__main__':
    practical_test64()

    