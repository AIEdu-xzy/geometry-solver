from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test72():
    link(D, E)
    link(E, F)
    link(D, F)
    link(D, A, B)
    link(E, B, C)
    link(F, C, A)

    set_length('AB', 1)
    set_length('EB', 1)
    set_length('CF', 1)
    is_equilateral_triangle('ABC')
    common_vertex_angles('D', ['E', 'B', 'F'])
    common_vertex_angles('E', ['D', 'C', 'F'])
    common_vertex_angles('F', ['D', 'A', 'E'])
    
    get_length('EF')

    return get_problem()
    

if __name__ == '__main__':
    practical_test72()

    