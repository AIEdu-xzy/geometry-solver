from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test77():
    link(A, B)
    link(B, D, C)
    link(A, C)
    link(A, D)

    set_length('AB', 7)
    set_length('AC', 4)
    set_length('BC', 6)
    split_angle('BAC', 'AD')
    
    get_length('BD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test77()

    