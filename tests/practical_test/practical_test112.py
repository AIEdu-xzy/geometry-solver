from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test112():
    link(A, B)
    link(A, D, C)
    link(B, D)
    link(B, C)
    
    set_angle('BAC', 80)
    set_length('AB', 1)
    set_length('BD', 1)
    set_length('CD', 1)
    common_vertex_angles('B', ['A', 'D', 'C'])
    
    get_angle('ACB')

    return get_problem()
    

if __name__ == '__main__':
    practical_test112()
