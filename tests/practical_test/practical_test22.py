from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, get_length, common_vertex_angles, get_problem


def practical_test22():
    link(A, D, B)
    link(A, E, C)
    link(B, C)
    link(C, F, D)
    link(B, F, E)

    set_angle('BAC', 50)
    set_angle('ACD', 40)
    set_angle('ABE', 28)

    common_vertex_angles('B', ['A', 'E', 'C'])
    common_vertex_angles('C', ['A', 'D', 'B'])

    get_angle('CFE')

    # assert result['answer'] == 62
    return get_problem()


if __name__ == '__main__':
    practical_test22()
    
