from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test122():
    link(A, C)
    link(A, D, B)
    link(B, C)
    link(C, D)
    
    set_angle('ACB', 90)
    set_angle('CDB', 90)
    set_angle('BAC', 30)
    set_length('BC', 1)
    common_vertex_angles('C', ['A', 'D', 'B'])
    
    get_length('BD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test122()
