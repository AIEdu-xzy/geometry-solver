from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test55():
    link(A, B)
    link(A, C)
    link(B, C)

    set_length('AB', 6)
    set_length('AC', 6)
    is_right_triangle('ABC', 'BAC')
    
    get_circumference('ABC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test55()

    