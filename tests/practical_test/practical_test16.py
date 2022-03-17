from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_length, common_vertex_angles, get_problem


def practical_test16():
    link(A, B)
    link(A, D, C)
    link(B, D)
    link(B, E, C)
    link(D, E)

    set_angle('BAC', 90)
    set_length('AB', 4)
    set_length('BD', 5)
    perpendicular('DE', 'BC')
    split_angle('ABC', 'BD', 0.5)

    common_vertex_angles('B', ['A', 'D', 'C'])

    get_length('AD')

    # assert result['answer'] == 3
    return get_problem()


if __name__ == '__main__':
    practical_test16()

