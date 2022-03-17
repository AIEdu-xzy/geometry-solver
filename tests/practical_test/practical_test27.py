from geometry_solver.easy_input.abc import A, B, C, D
from geometry_solver.easy_input import link, set_length, set_angle, split_line, perpendicular, get_angle, common_vertex_angles, get_angle, get_problem


def practical_test27():
    link(A, B)
    link(A, C)
    link(B, D, C)
    link(A, D)
    
    set_angle('ABD', 50)

    split_line('BC', 'D')

    set_length('AB', 1)
    set_length('AC', 1)

    common_vertex_angles('A', ['B', 'D', 'C'])

    get_angle('BAD')
    
    # assert result['answer'] == 40
    return get_problem()

if __name__ == '__main__':
    practical_test27()

    