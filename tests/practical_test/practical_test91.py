from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test91():
    link(A, E, B)
    link(A, D, C)
    link(C, B)
    link(D, E)
    link(B, D)

    set_angle('BAC', 56)
    set_angle('ACB', 88)
    split_angle('ABC', 'BD')
    perpendicular('AB', 'DE')
    
    get_angle('EDB')

    return get_problem()
    

if __name__ == '__main__':
    practical_test91()
