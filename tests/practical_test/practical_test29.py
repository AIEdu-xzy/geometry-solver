from geometry_solver.easy_input.abc import A, B, C, D
from geometry_solver.easy_input import link, set_length, set_angle, split_line, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, get_problem


def practical_test29():
    link(A, B)
    link(A, C)
    link(B, D, C)
    link(A, D)

    set_length('AB', 8)
    set_length('BD', 4)
    common_vertex_angles('A', ['B', 'D', 'C'])
    split_line('BC', 'D')
    set_angle('ABC', 60)
    
    get_length('AC')

    # assert result['answer'] == 8
    return get_problem()


if __name__ == '__main__':
    practical_test29()

