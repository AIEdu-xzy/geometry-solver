from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test99():
    link(A, B)
    link(A, C)
    link(C, E)
    link(B, E)
    link(A, D, P, E)
    link(C, P, B)
    link(C, D)

    line_equivalence('AC', 'BC')
    set_length('CD', 1)
    set_length('CE', 1)
    set_angle('ACB', 90)
    set_angle('DCE', 90)
    
    get_angle('CDA')

    return get_problem()
    

if __name__ == '__main__':
    practical_test99()
