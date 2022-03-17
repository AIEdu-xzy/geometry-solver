from geometry_solver.easy_input.abc import A, B, C, M, N
from geometry_solver.easy_input import link, set_length, get_length, perpendicular, split_line, get_problem


def practical_test5():
    link(A, B)
    link(A, N, C)
    link(B, M, C)
    link(M, N)

    set_length('AB', 5)
    set_length('AC', 5)
    set_length('BC', 6)

    perpendicular('MN', 'AC')
    split_line('BC', 'M', 0.5)
    
    get_length('MN')
    
    # assert result['answer'] == 2.4
    return get_problem()


if __name__ == '__main__':
    practical_test5()  

