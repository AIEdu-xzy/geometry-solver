from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test74():
    link(A, B)
    link(B, C)
    link(A, C)

    set_length('AB', 2)
    set_length('AC', 4)
    set_length('BC', 3)
    
    get_circumference('ABC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test74()

    