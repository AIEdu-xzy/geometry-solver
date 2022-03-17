from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test125():
    link(A, B)
    link(B, C)
    link(A, C)
    
    set_angle('ACB', 90)
    set_length('AC', 3)
    set_length('BC', 2)
    
    get_angle('ABC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test125()
