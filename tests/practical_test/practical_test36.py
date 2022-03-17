from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, get_problem


def practical_test36():
    link(A, D)
    link(A, E)
    link(D, C)
    link(E, C)
    link(D, B)
    link(E, B)
    link(D, E)

    set_angle('DAE', 60)
    
    set_length('BD', 2)
    set_length('BE', 2)
    set_length('AD', 3)
    set_length('AE', 3)

    split_angle('ADB', 'DC')
    split_angle('AEB', 'EC')

    common_vertex_angles('D', ['A', 'C', 'B', 'E'])
    common_vertex_angles('E', ['A', 'C', 'B', 'D'])

    get_angle('DBE')

    # assert abs(result['answer'] - 97.181) < 1e-3
    return get_problem()


if __name__ == '__main__':
    practical_test36()
    
