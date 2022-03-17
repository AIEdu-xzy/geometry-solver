from geometry_solver.easy_input.abc import A, B, C, D, E, F, G, H, P
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, get_problem


def practical_test38():
    link(A, G, H, B)
    link(B, D)
    link(D, H, P, C)
    link(C, E)
    link(E, P, G, F)
    link(F, A)

    set_angle('BAF', 20)
    set_angle('ABD', 40)
    set_angle('DCE', 60)
    set_angle('BDC', 80)
    set_angle('CEF', 90)
    
    get_angle('AFE')
    
    # assert result['answer'] == 70
    return get_problem()


if __name__ == '__main__':
    practical_test38()
    
