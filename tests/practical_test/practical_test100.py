from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test100():
    link(A, E, B)
    link(A, D, C)
    link(B, C, F)
    link(E, D, F)
    link(B, D)

    is_equilateral_triangle('ABC')
    split_line('AC', 'D')
    set_length('AE', 1)
    set_length('AC', 4)
    
    get_length('BF')

    return get_problem()
    

if __name__ == '__main__':
    practical_test100()
