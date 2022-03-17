from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test90():
    link(A, B, C)
    link(A, D, E)
    link(C, F, D)
    link(B, F, E)

    set_angle('ACD', 30)
    set_angle('AEB', 45)
    set_angle('CAE', 90)
    
    get_angle('BFD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test90()
