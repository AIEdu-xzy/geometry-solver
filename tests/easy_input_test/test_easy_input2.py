from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import link, parallel, set_angle, get_angle

def test_easy_input2():
    link(A, B)
    link(C, D)
    link(B, C)
    parallel('AB', 'CD')
    set_angle('ABC', 60)
    result = get_angle('BCD')
    print(result)
    
if __name__ == '__main__':
    test_easy_input2()
    
