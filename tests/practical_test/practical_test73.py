from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def practical_test73():
    link(C, A)
    link(C, B)
    link(C, D)
    link(A, D, B)

    is_right_triangle('ABC', 'ACB')
    set_length('AC', 900)
    set_length('BC', 1200)
    perpendicular('CD', 'AB')
    
    get_length('CD')

    return get_problem()
    

if __name__ == '__main__':
    practical_test73()

  