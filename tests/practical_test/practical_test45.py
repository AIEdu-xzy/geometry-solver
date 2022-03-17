from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, split_line, get_problem


def practical_test45():
    link(A, B)
    link(A, C)
    link(D, B)
    link(D, C)
    link(B, C, E)

    set_angle('BAC', 50)
    set_angle('ABC', 60)
    split_angle('ABC', 'BD')
    split_angle('ACE', 'CD')

    common_vertex_angles('B', ['A', 'D', 'E'])
    common_vertex_angles('C', ['A', 'D', 'E'])

    get_angle('BDC')

    # assert result['answer'] == 25
    return get_problem()

    
if __name__ == '__main__':
    practical_test45()

    