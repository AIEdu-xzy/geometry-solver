from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import link, perpendicular, set_angle, get_angle

def test_easy_input3():
    link(A, B)
    link(B, C)
    perpendicular('AB', 'BC')
    result = get_angle('ABC')
    print(result)
    
if __name__ == '__main__':
    test_easy_input3()

