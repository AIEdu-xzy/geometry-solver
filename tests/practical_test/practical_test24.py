from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, get_length, common_vertex_angles, get_problem


def practical_test24():
    link(A, B)
    link(A, C)
    link(B, C)
    link(B, D)
    link(C, D)
    link(B, E)
    link(C, E)

    set_angle('BAC', 42)
    set_angle('ABC', 70)

    split_angle('ABC', 'BD', 1/3)
    split_angle('ACB', 'CD', 1/3)
    split_angle('ABC', 'BE', 2/3)
    split_angle('ACB', 'CE', 2/3)

    common_vertex_angles('B', ['A', 'D', 'E', 'C'])
    common_vertex_angles('C', ['A', 'D', 'E', 'B'])

    get_angle('BDC')

    # assert result['answer'] == 88
    return get_problem()


if __name__ == '__main__':
    practical_test24()
    
