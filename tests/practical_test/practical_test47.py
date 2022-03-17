from geometry_solver.easy_input.abc import A, B, C, D, P
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, parallel, get_angle, common_vertex_angles, get_angle, get_length, split_line, get_problem


def practical_test47():
    link(A, B)
    link(A, P, D)
    link(B, P, C)
    link(C, D)

    set_length('AB', 4)
    set_length('CD', 6)
    set_length('AD', 10)
    set_angle('DAB', 30)
    set_angle('ADC', 30)
    set_angle('BCD', 45)
    set_angle('ABC', 45)

    get_length('AP')

    # assert result['answer'] == 4
    return get_problem()
    
    
if __name__ == '__main__':
    practical_test47()
    
    