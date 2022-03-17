from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test102():
    link(A, B)
    link(A, C)
    link(A, P)
    link(A, Q)
    link(B, P, Q, C)

    set_angle('ABC', 25)
    set_length('BP', 1)
    set_length('QC', 1)
    set_length('AP', 1)
    set_length('AQ', 1)
    
    get_angle('PAQ')

    return get_problem()
    

if __name__ == '__main__':
    practical_test102()
