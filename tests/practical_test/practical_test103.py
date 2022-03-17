from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, angle_equivalence, get_problem


def practical_test103():
    link(A, E, B)
    link(A, F, C)
    link(B, D, C)
    link(D, E)
    link(D, F)

    perpendicular('DE', 'AB')
    perpendicular('FD', 'BC')

    set_angle('AFD', 158)

    common_vertex_angles('D', ['B', 'E', 'F'])

    angle_equivalence('ABC', 'ACB')

    get_angle('EDF')

    # assert result['answer'] == 68
    return get_problem()


if __name__ == '__main__':
    practical_test103()
    
