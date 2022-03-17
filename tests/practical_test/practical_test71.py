from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test71():
    link(A, B)
    link(A, C)
    link(A, D)
    link(B, D, C)

    set_length('AB', 1)
    is_equilateral_triangle('ABC')
    perpendicular('AD', 'BC')
    
    get_length('AD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test71()

    