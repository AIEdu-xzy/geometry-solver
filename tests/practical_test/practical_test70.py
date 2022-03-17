from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test70():
    link(A, B)
    link(A, D, C)
    link(B, E, C)
    link(E, D)
    link(B, D)

    is_equilateral_triangle('ABC')
    set_length('AB', 8)
    split_line('AC', 'D')
    perpendicular('DE', 'BC')
    
    get_length('AD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test70()

  