from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test116():
    link(A, B)
    link(A, C)
    link(B, C)
    
    is_equilateral_triangle('ABC')
    set_length('AB', 4)
    
    get_area('ABC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test116()
