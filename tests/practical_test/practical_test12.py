from geometry_solver.easy_input.abc import A, B, C, D, E, F, G, P
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, parallel, get_angle, common_vertex_angles, angle_equivalence, get_problem



def practical_test12():
    link(A, C)
    link(A, E, P)
    link(A, F, G, D)
    link(B, F, E, C)
    link(B, G, P)
    link(B, D)

    set_angle('ACB', 32)
    set_angle('ADB', 28)
    set_angle('CBD', 60)

    angle_equivalence('CAP', 'DAP')
    angle_equivalence('CBP', 'DBP')
    
    common_vertex_angles('B', ['C', 'P', 'D'])
    common_vertex_angles('A', ['C', 'P', 'D'])

    get_angle('APB')

    # assert result['answer'] == 30
    return get_problem()

    
if __name__ == '__main__':
    practical_test12()
    
