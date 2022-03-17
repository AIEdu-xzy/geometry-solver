from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test95():
    link(A, E, B)
    link(A, C)
    link(B, D, F, C)
    link(E, F)
    link(A, F)
    link(E, D)

    set_angle('ACB', 90)
    set_angle('ABC', 30)
    set_length('BC', 3)
    perpendicular('DE', 'BC')
    is_right_triangle('AEF', 'AFE')
    
    get_length('AC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test95()
