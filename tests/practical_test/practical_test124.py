from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test124():
    link(A, D, C)
    link(A, B)
    link(B, C)
    link(B, E, D)
    link(E, C)
    
    set_angle('ACB', 72)
    set_angle('BAC', 36)
    split_angle('ABC', 'BD')
    split_angle('BCD', 'CE')
    
    get_angle('CED')

    return get_problem()
    

if __name__ == '__main__':
    practical_test124()
