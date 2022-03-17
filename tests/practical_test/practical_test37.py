from geometry_solver.easy_input.abc import A, B, C, D, E, F, G, H, I, J
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, get_problem


def practical_test37():
    link(A, F, H, C)
    link(C, J, I, E)
    link(E, G, F, B)
    link(B, H, J, D)
    link(D, I, G, A)

    set_angle('CAD', 10)
    set_angle('EBD', 20)
    set_angle('ACE', 30)
    set_angle('ADB', 40)

    get_angle('BEC')

    # assert result['answer'] == 80
    return get_problem()


if __name__ == '__main__':
    practical_test37()
        
