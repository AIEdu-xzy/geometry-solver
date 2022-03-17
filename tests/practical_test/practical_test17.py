from geometry_solver.easy_input.abc import A, B, C, D
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, line_equivalence, get_problem



def practical_test17():
    link(A, B)
    link(A, D, C)
    link(B, D)
    link(B, C)

    set_angle('BAC', 40)

    common_vertex_angles('B', ['A', 'D', 'C'])

    # Set as unit length.
    set_length('AB', 1)
    
    line_equivalence('AB', 'AC')
    line_equivalence('BD', 'BC')

    get_angle('ABD')

    # assert result['answer'] == 30
    return get_problem()


if __name__ == '__main__':
    practical_test17()

