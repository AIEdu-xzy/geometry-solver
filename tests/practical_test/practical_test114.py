from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test114():
    link(A, D, B)
    link(B, E, C)
    link(A, C)
    link(D, E)
    
    is_right_triangle('ABC', 'ABC')
    set_angle('CED', 165)
    
    get_angle('ADE')

    return get_problem()
    

if __name__ == '__main__':
    practical_test114()
