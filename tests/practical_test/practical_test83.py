from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test83():
    link(A, C)
    link(B, C)
    link(A, D, B)
    link(C, D)

    set_angle('ACB', 90)
    set_angle('BAC', 30)
    set_length('AB', 24)
    perpendicular('CD', 'AB')
    
    get_length('BD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test83()
