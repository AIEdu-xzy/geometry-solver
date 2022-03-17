from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test60():
    link(A, B, D)
    link(A, C)
    link(B, C)
    link(B, O, E)
    link(C, O, D)
    link(C, E)
    link(D, E)

    set_length('AC', 3)
    set_length('BC', 3)
    set_angle('ACB', 90)
    set_angle('DCE', 90)
    split_line('AD', 'B')
    line_equivalence('CD', 'CE')
    common_vertex_angles('D', ['E', 'C', 'A'])
    common_vertex_angles('E', ['C', 'B', 'D'])
    common_vertex_angles('C', ['E', 'D', 'B'])
    common_vertex_angles('C', ['A', 'B', 'D'])
    
    get_length('BE')

    return get_problem()
    

if __name__ == '__main__':
    practical_test60()
