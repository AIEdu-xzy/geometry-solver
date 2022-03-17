from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test59():
    link(A, M, P, B)
    link(A, Q, C)
    link(B, C)
    link(M, Q)
    link(P, Q)

    set_length('AM', 1)
    set_length('MQ', 1)
    set_length('QP', 1)
    set_angle('ACB', 74)
    is_right_triangle('ABC', 'ABC')
    
    get_angle('QPB')

    return get_problem()
    

if __name__ == '__main__':
    practical_test59()

