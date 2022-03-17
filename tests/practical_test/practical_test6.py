from geometry_solver.easy_input.abc import A, B, C, M, N, O
from geometry_solver.easy_input import link, set_length, get_length, split_angle, parallel, get_angle, common_vertex_angles, get_circumference, get_problem


def practical_test6():
    link(A, M, B)
    link(A, N, C)
    link(B, C)
    link(B, O)
    link(C, O)
    link(M, O, N)

    set_length('AB', 12)
    set_length('AC', 18)
    set_length('BC', 24)

    split_angle('ABC', 'BO', 0.5)
    split_angle('ACB', 'CO', 0.5)
    
    parallel('MN', 'BC')

    common_vertex_angles('B', ['A', 'O', 'C'])
    common_vertex_angles('C', ['A', 'O', 'B'])
    
    get_circumference('AMN')

    # assert result['answer'] == 30
    return get_problem()


if __name__ == '__main__':
    practical_test6()  

