from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, get_length, common_vertex_angles, get_problem


def practical_test18():
    link(A, B)
    link(A, C)
    link(B, D, E, C)
    link(A, F, D)
    link(B, F)
    link(A, E)

    common_vertex_angles('A', ['B', 'D', 'E', 'C'])
    common_vertex_angles('B', ['A', 'F', 'C'])

    perpendicular('AD', 'BC')

    set_angle('AED', 62)
    set_angle('BAC', 90)
    set_angle('ACB', 45)

    # Set as unit length.
    set_length('AF', 1)
    set_length('EC', 1)

    get_angle('DBF')

    # assert result['answer'] == 28
    return get_problem()


if __name__ == '__main__':
    practical_test18()

