from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test97():
    link(A, E, B)
    link(A, D, C)
    link(D, E)
    link(B, D)
    link(B, C)

    line_equivalence('AB', 'AC')
    set_angle('BAC', 30)
    split_angle('ADB', 'DE')
    set_length('AB', 2)
    split_line('AB', 'E')
    perpendicular('AB', 'DE')
    
    get_angle('CBD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test97()
