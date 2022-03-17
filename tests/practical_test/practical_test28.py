from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_problem


def practical_test28():
    link(A, B)
    link(A, E, C)
    link(B, D, C)
    link(B, F, E)
    link(A, F, D)

    set_angle('BAD', 45)
    set_angle('ACB', 60)

    perpendicular('AD', 'BC')
    perpendicular('BE', 'AC')

    common_vertex_angles('A', ['B', 'D', 'C'])
    common_vertex_angles('B', ['A', 'E', 'C'])

    get_angle('BFD')

    # assert result['answer'] == 60
    return get_problem()


if __name__ == '__main__':
    practical_test28()
    
    