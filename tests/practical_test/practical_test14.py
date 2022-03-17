from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, parallel, get_angle, common_vertex_angles, angle_equivalence, get_problem



def practical_test14():
    link(A, B)
    link(A, D, C)
    link(B, C)
    link(B, E, D)
    link(C, E)

    set_angle('ABD', 30)
    set_angle('CBD', 30)
    set_angle('BAC', 80)
    
    common_vertex_angles('B', ['A', 'D', 'C'])
    common_vertex_angles('C', ['A', 'E', 'B'])
    
    angle_equivalence('BCE', 'ACE')
    
    get_angle('BEC')

    # assert result['answer'] == 130
    return get_problem()


if __name__ == '__main__':
    practical_test14()

