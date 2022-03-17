from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, parallel, get_angle, common_vertex_angles, get_problem


def practical_test15():
    link(A, E, B)
    link(A, D, C)
    link(B, C)
    link(B, D)
    link(D, E)

    parallel('ED', 'BC')
    split_angle('ABC', 'BD', 0.5)
    set_angle('BAC', 60)
    set_angle('BDC', 95)

    common_vertex_angles('B', ['A', 'D', 'C'])
    common_vertex_angles('D', ['E', 'B', 'C'])

    get_angle('DBC')

    # assert result['answer'] == 35
    return get_problem()


if __name__ == '__main__':
    practical_test15()
    
