from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test67():
    link(A, B)
    link(B, C)
    link(A, C)

    line_equivalence('AB', 'AC')
    set_angle('BAC', 40)
    set_angle('ABC', 70)
    
    get_angle('ACB')

    return get_problem()
    

if __name__ == '__main__':
    practical_test67()

    