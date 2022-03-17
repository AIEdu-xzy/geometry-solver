from geometry_solver.easy_input.abc import A, B, C, P
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, split_line, line_equivalence, get_problem


def practical_test44():
    link(A, C)
    link(A, P)
    link(A, B)
    link(C, P, B)
    
    set_angle('ACB', 90)
    set_length('AC', 3)
    set_length('BC', 4)
    split_line('BC', 'P', 0.5)
    
    common_vertex_angles('A', ['C', 'P', 'B'])
    
    get_length('AP')

    # assert result['answer'] == 60
    return get_problem()

    
if __name__ == '__main__':
    practical_test44()

