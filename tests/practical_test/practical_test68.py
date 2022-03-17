from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test68():
    link(A, B)
    link(B, C)
    link(A, C)

    is_right_triangle('ABC', 'BAC')
    set_angle('ABC', 30)
    
    get_angle('ACB')

    return get_problem()
    

if __name__ == '__main__':
    practical_test68()

    