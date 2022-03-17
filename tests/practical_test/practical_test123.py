from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test123():
    link(A, E, C)
    link(A, D, B)
    link(B, C)
    link(D, E)
    link(B, E)
    
    set_angle('ACB', 90)
    set_length('AC', 18)
    set_length('EC', 5)
    line_equivalence('AE', 'BE')
    common_vertex_angles('B', ['A', 'E', 'C'])
    split_angle('ABC', 'BE')
    
    get_length('BE')

    return get_problem()
    

if __name__ == '__main__':
    practical_test123()
