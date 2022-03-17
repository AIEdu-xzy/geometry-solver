from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test76():
    link(C, A)
    link(C, B)
    link(C, D)
    link(C, E)
    link(A, D, E, B)
    
    set_angle('ACB', 90)
    set_angle('DCE', 45)
    set_length('BE', 2)
    set_length('CA', 4)
    set_length('CB', 4)
    
    get_length('CE')

    return get_problem()
    

if __name__ == '__main__':
    practical_test76()

    