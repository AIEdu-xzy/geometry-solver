from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test101():
    link(A, D, B)
    link(A, F, C)
    link(D, F)
    link(F, H)
    link(B, H, C)

    is_equilateral_triangle('ABC')
    split_line('AB', 'D')
    perpendicular('DF', 'AC')
    perpendicular('FH', 'BC')
    set_length('AC', 4)
    
    get_length('BH')

    return get_problem()
    

if __name__ == '__main__':
    practical_test101()
