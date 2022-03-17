from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test87():
    link(A, B)
    link(A, E, C)
    link(B, D, C)
    link(A, D)
    link(D, E)

    is_equilateral_triangle('ABC')
    set_length('AB', 6)
    split_line('BC', 'D')
    set_angle('EDA', 30)
    
    get_length('ED')

    return get_problem()
    

if __name__ == '__main__':
    practical_test87()
