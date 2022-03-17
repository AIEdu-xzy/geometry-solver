from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, get_length, common_vertex_angles, get_problem


def practical_test21():
    link(A, B)
    link(A, C)
    link(A, D)
    link(A, E)
    link(B, E, D, C)

    perpendicular('AD', 'BC')
    split_angle('BAC', 'AE')

    set_angle('ABC', 42)
    set_angle('ACB', 84)

    common_vertex_angles('A', ['B', 'E', 'D', 'C'])

    get_angle('AEC')

    # assert result['answer'] == 69
    return get_problem()


if __name__ == '__main__':
    practical_test21()

