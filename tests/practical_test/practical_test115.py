from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test115():
    link(A, B)
    link(A, O, C)
    link(D, O, B)
    link(D, C)
    link(B, C)
    
    set_angle('BAC', 72)
    set_angle('BDC', 72)
    set_angle('ACB', 36)
    set_angle('DBC', 36)
    set_length('BC', 1)
    
    get_length('BD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test115()
