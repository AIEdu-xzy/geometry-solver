from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test117():
    link(A, B)
    link(A, D, C)
    link(D, B)
    link(D, E)
    link(B, C, E)
    
    is_equilateral_triangle('ABC')
    set_length('AB', 6)
    split_angle('ABE', 'BD')
    line_equivalence('CD', 'CE')
    
    get_length('CE')

    return get_problem()
    

if __name__ == '__main__':
    practical_test117()
