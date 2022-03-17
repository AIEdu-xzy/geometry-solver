from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, get_problem


def practical_test31():
    link(A, B)
    link(A, C)
    link(D, B, C, E)
    set_angle('BAC', 80)
    set_angle('ACE', 140)
    
    get_angle('ABD')
    
    # assert result['answer'] == 120
    return get_problem()


if __name__ == '__main__':
    practical_test31()
    
