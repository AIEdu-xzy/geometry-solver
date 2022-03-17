from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test88():
    link(A, D, B)
    link(A, F, C)
    link(B, H, C)
    link(D, F)
    link(H, F)

    split_line('AB', 'D')
    perpendicular('DF', 'AC')
    perpendicular('FH', 'BC')
    is_equilateral_triangle('ABC')
    set_length('AB', 8)
    
    get_length('BH')

    return get_problem()
    

if __name__ == '__main__':
    practical_test88()
