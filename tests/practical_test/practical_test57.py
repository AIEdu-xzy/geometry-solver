from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test57():
    link(A, B)
    link(A, C)
    link(A, D)
    link(B, D, C)

    set_length('AC', 2)
    set_length('BC', 2)
    set_angle('ACB', 120)
    is_equilateral_triangle('ABC')
    perpendicular('AD', 'BC')
    
    get_length('AD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test57()

    