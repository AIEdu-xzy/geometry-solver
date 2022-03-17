from geometry_solver.easy_input.abc import A, B, C, D, E, F, O
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, get_length, common_vertex_angles, get_problem


def practical_test23():
    link(A, F, B)
    link(A, E, C)
    link(B, C)
    link(B, O, E)
    link(C, O, F)

    perpendicular('CF', 'AB')
    perpendicular('BE', 'AC')

    set_angle('BAC', 50)

    common_vertex_angles('B', ['A', 'E', 'C'])
    common_vertex_angles('C', ['A', 'F', 'B'])

    get_angle('BOC')

    # assert result['answer'] == 130
    return get_problem()


if __name__ == '__main__':
    practical_test23()

