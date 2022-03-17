from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test86():
    link(A, B)
    link(A, D, C)
    link(B, C)
    link(B, D)

    set_length('BD', 1)
    line_equivalence('BD', 'AD')
    split_angle('ABC', 'BD')
    set_angle('ACB', 90)
    set_angle('CBD', 30)
    
    get_angle('BAC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test86()
