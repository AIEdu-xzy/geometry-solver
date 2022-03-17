from geometry_solver.easy_input.abc import A, B, C, D, O
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, get_problem


def practical_test30():
    link(O, A)
    link(O, D)
    link(O, B)
    link(O, C)
    link(A, B)
    link(D, C)

    set_angle('AOB', 90)
    set_angle('DOC', 90)
    set_angle('BOD', 60)

    common_vertex_angles('O', ['A', 'D', 'B', 'C'])
    
    get_angle('AOC')

    # assert result['answer'] == 120
    return get_problem()
    

if __name__ == '__main__':
    practical_test30()
    
    