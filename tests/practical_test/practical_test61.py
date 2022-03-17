from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test61():
    link(A, B)
    link(A, C)
    link(B, C)

    set_length('AC', 5)
    set_length('BC', 5)
    set_length('AB', 6)
    
    get_area('ABC')

    return get_problem()
    

if __name__ == '__main__':
    practical_test61()

    