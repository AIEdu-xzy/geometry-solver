from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import link, set_angle, get_angle

def test_easy_input1():
    link(A, B)
    link(B, C)
    link(A, C)
    set_angle('BAC', 60)
    set_angle('ACB', 50)
    result = get_angle('ABC')
    print(result)
    
if __name__ == '__main__':
    test_easy_input1()
    
