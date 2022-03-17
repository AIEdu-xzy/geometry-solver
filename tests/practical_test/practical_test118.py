from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test118():
    link(A, B)
    link(A, D, C)
    link(B, C)
    link(A, E)
    link(D, E)
    
    is_equilateral_triangle('ABC')
    is_equilateral_triangle('ADE')
    set_length('AB', 2)
    set_length('AD', 1)
    
    get_length('AE')

    return get_problem()
    

if __name__ == '__main__':
    practical_test118()
