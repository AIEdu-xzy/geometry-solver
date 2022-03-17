from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, parallel, get_angle, common_vertex_angles, get_angle, get_length, split_line, get_problem


def practical_test49():
    link(A, D, B)
    link(A, E, C)
    link(D, E)
    link(B, C)

    set_angle('ADE', 60)
    set_angle('ABC', 60)
    set_angle('BAC', 30)
    set_length('DE', 4)

    split_line('AB', 'D', 1/3)
    
    get_length('BC')

    # assert result['answer'] == 12
    return get_problem()
    
    
if __name__ == '__main__':
    practical_test49()
    
    