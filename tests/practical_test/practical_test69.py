from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test69():
    link(A, B)
    link(B, C)
    link(A, C)

    line_equivalence('AB', 'AC')
    set_angle('ABC', 65)
    
    get_angle('BAC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test69()

    