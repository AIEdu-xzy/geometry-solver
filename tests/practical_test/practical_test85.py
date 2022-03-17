from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test85():
    link(A, B)
    link(A, D, C)
    link(B, C)
    link(B, D)

    line_equivalence('AB', 'AC')
    split_angle('ABC', 'BD')
    split_line('BC', 'D')
    set_length('AB', 1)
    set_angle('BAC', 36)
    
    get_length('BD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test85()
