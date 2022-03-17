from geometry_solver.easy_input.abc import A, B, C, D, F
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_length, get_problem


def practical_test9():
    link(A, C)
    link(A, D, B)
    link(B, F, C)
    link(D, F)

    set_angle('ACB', 90)

    perpendicular('DF', 'AB')

    set_length('AC', 1)
    set_length('AD', 1)
    set_length('BC', 1)
    
    get_length('BF')

    # assert abs(result['answer'] - (2 - 2**(1/2))) < 1e-3
    return get_problem()


if __name__ == '__main__':
    practical_test9()
    
