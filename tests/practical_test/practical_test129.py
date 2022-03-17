from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test129():
    link(A, B)
    link(A, C)
    link(A, D)
    link(B, D, C)
    
    line_equivalence('AB', 'AC')
    set_length('BC', 10)
    set_angle('ABC', 36)
    split_line('BC', 'D')

    get_length('AD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test129()
