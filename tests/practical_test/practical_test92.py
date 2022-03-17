from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test92():
    link(A, D, B, E)
    link(E, F)
    link(B, C)
    link(D, F)
    link(A, C)

    set_length('AC', 4)
    set_length('AB', 4.5)
    set_angle('EAC', 26)
    set_angle('AEF', 74)
    parallel('DF', 'AC')
    
    get_angle('EFD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test92()
