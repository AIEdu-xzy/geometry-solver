from geometry_solver.easy_input.abc import A, B, C, D, F
from geometry_solver.easy_input import link, set_angle, get_angle, split_angle, common_vertex_angles, perpendicular, get_problem


def practical_test4():
    link(A, B)
    link(A, F)
    link(A, D)
    link(A, C)
    link(B, F, D, C)

    set_angle('ABC', 36)
    set_angle('ACB', 76)

    split_angle('BAC', 'AF', ratio=0.5)
    common_vertex_angles('A', ['B', 'F', 'D', 'C'])
    perpendicular('AD', 'BC')

    get_angle('DAF')

    # assert result['answer'] == 20
    return get_problem()


if __name__ == '__main__':
    practical_test4()

