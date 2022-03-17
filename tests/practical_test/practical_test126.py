from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test126():
    link(A, B)
    link(A, C)
    link(A, D, O, E)
    link(B, C)
    link(B, D)
    link(C, D)
    link(B, E)
    link(C, E)
    
    set_angle('ACB', 90)
    set_angle('ADC', 150)
    set_angle('CBD', 15)
    line_equivalence('CE', 'CA')
    set_length('AD', 3)
    set_length('CD', 1)
    
    get_length('AC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test126()
