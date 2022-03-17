from geometry_solver.easy_input.abc import A, B, C, D
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, get_length, common_vertex_angles, get_problem


def practical_test19():
    link(A, B)
    link(A, C)
    link(B, C, D)

    set_angle('ABC', 40)
    set_angle('ACD', 120)

    get_angle('BAC')

    # assert result['answer'] == 80
    return get_problem()


if __name__ == '__main__':
    practical_test19()

