from geometry_solver.easy_input.abc import A, B, C, D
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, split_line, get_problem


def practical_test41():
    link(A, B)
    link(B, D)
    link(B, C)
    link(A, D, C)

    set_length('AB', 1)
    set_length('BD', 1)
    set_length('CD', 1)
    set_angle('BDC', 110)
    
    get_angle('ABC')

    # assert result['answer'] == 75
    return get_problem()
    

if __name__ == '__main__':
    practical_test41()
    
    