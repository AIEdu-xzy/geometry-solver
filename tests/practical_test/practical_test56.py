from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test56():
    link(A, B)
    link(A, C)
    link(B, C)

    set_angle('ABC', 25)
    is_right_triangle('ABC', 'BAC')
    
    get_angle('ACB')

    return get_problem()
    

if __name__ == '__main__':
    practical_test56()

    