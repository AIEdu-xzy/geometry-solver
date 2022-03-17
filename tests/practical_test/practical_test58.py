from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test58():
    link(A, B)
    link(C, D)
    link(B, C, E)
    link(A, D, E)

    set_length('CD', 20)
    set_length('AB', 30)
    set_length('CE', 20)
    set_angle('DCE', 90)
    is_right_triangle('ABE', 'ABE')
    parallel('AB', 'DC')
    
    get_area('CDE')

    return get_problem()
    

if __name__ == '__main__':
    practical_test58()

