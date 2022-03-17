from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, split_line, get_problem


def practical_test42():
    link(A, B)
    link(D, A, E)
    link(B, E, C)
    link(D, C)

    split_line('BC', 'E', 0.5)
    
    set_length('AE', 1)
    set_length('BE', 1)

    set_angle('BAE', 30)
    set_angle('CDE', 30)

    get_length('CD')

    # assert result['answer'] == 1.732
    return get_problem()
    

if __name__ == '__main__':
    practical_test42()

