from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, get_problem


def practical_test33():
    link(A, F, B)
    link(D, C, B)
    link(F, E, D)
    link(A, E ,C)

    set_angle('BAC', 35)
    set_angle('BDF', 42)

    perpendicular('DF', 'AB')

    get_angle('ACD')

    # assert result['answer'] == 83
    return get_problem()


if __name__ == '__main__':
    practical_test33()

