from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test119():
    link(A, B)
    link(A, E, C)
    link(B, D, C)
    link(A, D)
    link(D, E)
    
    split_line('BC', 'D')
    set_length('BC', 4)
    set_length('CE', 2)
    set_angle('ACB', 60)
    
    get_length('DE')

    return get_problem()
    

if __name__ == '__main__':
    practical_test119()
