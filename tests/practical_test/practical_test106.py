from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test106():
    link(A, E, B)
    link(A, F)
    link(A, D, C)
    link(B, C, F)
    link(F, D, E)
    link(B, D)
    
    line_equivalence('BC', 'BD')
    line_equivalence('AB', 'AC')
    set_angle('BDC', 36)
    
    get_angle('ACB')

    return get_problem()
    

if __name__ == '__main__':
    practical_test106()
