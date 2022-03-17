from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_problem


def practical_test89():
    link(A, E, C)
    link(B, D, C)
    link(A, B)
    link(A, F, D)
    link(B, F, E)

    set_angle('ACB', 70)
    set_angle('ABC', 48)

    split_angle('BAC', 'AD', 0.5)
    
    perpendicular('AC', 'BE')

    common_vertex_angles('A', ['B', 'D', 'C'])
    common_vertex_angles('B', ['A', 'E', 'C'])
    
    get_angle('BFD')

    return get_problem()


if __name__ == '__main__':
    practical_test89()
