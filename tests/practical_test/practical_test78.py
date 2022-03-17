from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test78():
    link(A, B)
    link(B, C)
    link(C, D)
    link(A, D)
    link(A, C)

    set_length('AB', 3)
    set_length('BC', 4)
    perpendicular('AB', 'BC')
    
    get_length('AC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test78()

    