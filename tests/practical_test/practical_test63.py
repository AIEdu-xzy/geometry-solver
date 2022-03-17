from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test63():
    link(A, B)
    link(B, C)
    link(A, C)

    set_length('AB', 10)
    set_length('AC', 12)
    set_angle('ACB', 72)
    set_angle('BAC', 50)
    
    get_length('BC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test63()

    