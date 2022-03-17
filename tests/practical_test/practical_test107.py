from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test107():
    link(A, E, B)
    link(A, D, C)
    link(B, C)
    link(B, O, D)
    link(C, O, E)
    
    perpendicular('CE', 'AB')
    perpendicular('BD', 'AC')
    set_length('OB', 2)
    set_length('OC', 2)
    set_length('AB', 3)
    set_angle('ABC', 60)
    set_angle('ACB', 60)
    
    get_length('AC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test107()
