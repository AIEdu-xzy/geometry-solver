from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test81():
    link(A, B)
    link(B, F, C)
    link(A, E, C)
    link(B, E)
    link(E, F)

    set_length('AC', 7)
    set_length('AB', 6)
    set_length('BC', 8)
    split_line('BC', 'F', 1/3)
    split_line('AC', 'E', 1/3)
    
    get_area('BFE')

    return get_problem()
    

if __name__ == '__main__':
    practical_test81()
