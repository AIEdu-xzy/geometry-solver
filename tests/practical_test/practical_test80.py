from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test80():
    link(A, B)
    link(B, C)
    link(A, C)

    set_length('AC', 4)
    set_length('AB', 3)
    is_right_triangle('BAC', 'BAC')
    
    get_length('BC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test80()
