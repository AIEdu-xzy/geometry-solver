from geometry_solver.easy_input.abc import A, B, C, D, E, M, N
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, split_line, get_problem


def practical_test43():
    link(A, B)
    link(A, C)
    link(B, D, C)
    link(A, D)

    split_line('BC', 'D')
    set_angle('BAC', 90)
    set_length('AB', 4)
    set_length('AC', 3)

    get_length('AD')

    # assert result['answer'] == 2.5
    return get_problem()
    
    
if __name__ == '__main__':
    practical_test43()

    