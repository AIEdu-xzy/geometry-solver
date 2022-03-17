from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test79():
    link(A, B)
    link(B, D, C)
    link(A, C)
    link(A, D)

    is_right_triangle('ABC', 'BAC')
    perpendicular('AD', 'BC')
    set_length('AB', 5)
    set_length('AC', 12)
    
    get_length('AD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test79()

    