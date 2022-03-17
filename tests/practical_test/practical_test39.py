from geometry_solver.easy_input.abc import A, B, C, D, F
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, get_problem


def practical_test39():
    link(A, F, B)
    link(A, C)
    link(B, D, C)
    link(D, F)
    link(A, D)

    split_angle('BAC', 'AD', 0.5)

    set_length('AB', 4)
    set_length('AC', 3)
    set_length('BC', 5)

    common_vertex_angles('A', ['B', 'D', 'C'])
    common_vertex_angles('D', ['B', 'F', 'A'])

    split_angle('BAC', 'AD')
    
    get_length('CD')
    
    # assert result['answer'] == 2.143
    return get_problem()


if __name__ == '__main__':
    practical_test39()    
        
