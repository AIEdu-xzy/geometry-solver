from geometry_solver.easy_input.abc import A, B, C, D, E, P, M, N
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, split_line, get_problem


def practical_test46():
    link(B, D, A)
    link(B, P)
    link(B, E, C)
    link(P, D)
    link(P, E)

    split_angle('ABC', 'BP', 0.5)

    set_length('DB', 1)
    set_length('DP', 1.2)
    set_length('BP', 3 ** (1/2))
    set_length('BE', 2)

    common_vertex_angles('B', ['A', 'P', 'C'])

    get_angle('BEP')

    # assert result['answer'] == 30
    return get_problem()
    
    
if __name__ == '__main__':
    practical_test46()
    
