from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test54():
    link(A, C)
    link(A, D, E, B)
    link(C, D)
    link(C, E)
    link(C, B)

    set_length('AC', 1)
    set_length('BC', 2)
    set_angle('ACB', 120)
    is_equilateral_triangle('CDE')
    
    get_length('AD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test54()

    