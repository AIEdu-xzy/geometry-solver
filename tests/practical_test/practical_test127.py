from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test127():
    link(A, D, B)
    link(A, E, C)
    link(B, C)
    link(D, F, E)
    link(B, F)
    link(C, F)
    
    parallel('DE', 'BC')
    split_angle('ABC', 'BF')
    split_angle('ACB', 'FC')
    set_angle('ABC', 60)
    set_angle('ACB', 60)
    set_length('BF', 1)

    get_length('CF')

    return get_problem()
    

if __name__ == '__main__':
    practical_test127()
