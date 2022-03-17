from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test51():
    link(A, B)
    link(A, C)
    link(B, C)

    line_equivalence('AB', 'AC')
    set_length('AC', 6)
    set_length('BC', 5)
    
    get_circumference('ABC')

    return get_problem()
    
    
if __name__ == '__main__':
    practical_test51()

    