from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, parallel, get_angle, get_length, common_vertex_angles, get_problem


def practical_test20():
    link(A, F, B)
    link(A, E)
    link(C, F, E)
    link(C, D)

    set_angle('EAB', 20)
    set_angle('AEC', 35)

    parallel('AB', 'CD')

    get_angle('ECD')

    # assert result['answer'] == 55
    return get_problem()


if __name__ == '__main__':
    practical_test20()
    
