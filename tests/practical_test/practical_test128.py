from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test128():
    link(A, B)
    link(A, C)
    link(B, C)
    link(O, A)
    link(O, B)
    link(O, C)
    
    set_length('AB', 20)
    set_length('BC', 30)
    set_length('AC', 40)
    split_angle('ABC', 'BO')
    split_angle('ACB', 'CO')
    split_angle('BAC', 'AO')

    get_length('CO')

    return get_problem()
    

if __name__ == '__main__':
    practical_test128()
