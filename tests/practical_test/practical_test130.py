from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test130():
    link(A, B)
    link(A, C)
    link(A, D)
    link(B, D, C)
    
    line_equivalence('AB', 'AC')
    set_length('CD', 3)
    set_angle('CAB', 35)
    set_angle('CBA', 35)
    split_line('BC', 'D')

    get_length('AC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test130()
