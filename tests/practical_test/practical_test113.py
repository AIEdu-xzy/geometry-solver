from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test113():
    link(D, A, B)
    link(A, E)
    link(A, C)
    link(B, C)
    
    set_angle('BAC', 90)
    set_angle('ACB', 45)
    line_equivalence('AB', 'AC')
    parallel('AE', 'BC')
    
    get_angle('DAE')

    return get_problem()
    

if __name__ == '__main__':
    practical_test113()
