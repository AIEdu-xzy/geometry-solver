from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test98():
    link(A, B)
    link(A, E, C)
    link(B, D, C)
    link(A, D)
    link(D, E)

    is_equilateral_triangle('ABC')
    split_angle('BAC', 'AD')
    set_length('AE', 1)
    set_length('AD', 1)
    
    get_angle('EDC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test98()
