from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test53():
    link(A, B)
    link(A, C)
    link(B, C)

    set_length('AB', 5)
    set_length('AC', 12)
    set_angle('BAC', 90)
    
    get_length('BC')

    return get_problem()
    
    
if __name__ == '__main__':
    practical_test53()

    