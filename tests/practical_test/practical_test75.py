from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test75():
    link(B, D, C)
    link(B, A, E)
    link(E, C)
    link(A, C)
    link(A, D)

    split_line('BE', 'A')
    split_line('BC', 'D')
    split_angle('BAC', 'AD')
    set_length('BC', 8)
    set_length('AD', 3)
    parallel('CE', 'AD')
    perpendicular('CE', 'BC')
    
    get_length('CE')

    return get_problem()
    

if __name__ == '__main__':
    practical_test75()

    