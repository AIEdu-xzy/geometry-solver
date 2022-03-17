from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test84():
    link(A, B)
    link(A, E, C)
    link(A, D)
    link(B, D, C)
    link(D, E)

    is_equilateral_triangle('ABC')
    line_equivalence('AD', 'AE')
    split_line('BC', 'D')
    set_length('AB', 1)
    
    get_angle('EDC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test84()
