from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test108():
    link(A, C)
    link(A, D)
    link(A, F, B)
    link(C, B)
    link(C, D, F, E)
    link(B, E)
    link(B, D)
    
    set_length('BE', 3)
    set_length('DE', 5)
    line_equivalence('AC', 'BC')
    is_right_triangle('ABC', 'ACB')
    perpendicular('AD', 'CE')
    perpendicular('BE', 'CE')
    
    get_length('BD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test108()
