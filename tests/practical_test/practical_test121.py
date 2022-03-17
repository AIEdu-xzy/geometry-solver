from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test121():
    link(A, B)
    link(A, E, C)
    link(A, P)
    link(A, D)
    link(B, D, E, P)
    link(P, C)
    link(B, C)
    
    is_equilateral_triangle('ABC')
    set_length('AD', 3)
    set_length('BD', 3)
    set_angle('ADB', 150)
    
    get_length('AC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test121()
