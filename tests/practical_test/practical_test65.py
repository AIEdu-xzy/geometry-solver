from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test65():
    link(A, B)
    link(A, E, C)
    link(B, D, C)
    link(A, D)
    link(D, E)

    set_length('AB', 6)
    set_length('BC', 8)
    set_angle('ACB', 72)
    set_angle('BAC', 50)
    is_right_triangle('ABC', 'ABC')
    perpendicular('AC', 'DE')
    common_vertex_angles('D', ['B', 'A', 'E'])
    common_vertex_angles('A', ['B', 'D', 'C'])
    split_angle('BAC', 'AD')
    split_angle('BDE', 'AD')
    line_equivalence('BD', 'DE')
    
    get_length('BD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test65()

    