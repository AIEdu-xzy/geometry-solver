from geometry_solver.easy_input.abc import A, B, C, O
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_problem


def practical_test8():
    link(A, B)
    link(A, C)
    link(B, C)
    link(B, O)
    link(C, O)

    set_angle('BOC', 136)
    set_angle('ABC', 36)

    split_angle('ABC', 'BO', 0.5)
    split_angle('ACB', 'CO', 0.5)

    common_vertex_angles('B', ['A', 'O', 'C'])
    common_vertex_angles('C', ['A', 'O', 'B'])

    get_angle('BAC')

    # assert result['answer'] == 92
    return get_problem()


if __name__ == '__main__':
    practical_test8()
    
