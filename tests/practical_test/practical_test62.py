from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test62():
    link(A, C)
    link(A, D, B)
    link(B, C)
    link(C, D)

    set_length('AC', 3)
    set_length('BC', 4)
    set_length('AB', 5)
    set_angle('ACB', 90)
    perpendicular('CD', 'AB')
    
    get_length('CD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test62()

    