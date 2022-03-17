from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test93():
    link(A, B)
    link(A, D, C)
    link(B, C)
    link(B, D)

    set_length('BC', 6)
    set_length('AB', 8)
    set_length('AC', 10)
    set_angle('CBA', 90)
    perpendicular('BD', 'AC')
    
    get_length('BD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test93()
