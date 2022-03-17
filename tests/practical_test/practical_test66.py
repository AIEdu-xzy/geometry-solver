from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test66():
    link(A, B)
    link(B, D, C)
    link(A, C)
    link(A, D)

    set_length('AC', 4)
    set_length('AB', 4)
    split_line('BC', 'D')
    is_right_triangle('BAC', 'BAC')
    
    get_length('AD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test66()

  