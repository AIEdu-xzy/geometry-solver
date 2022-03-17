from geometry_solver.easy_input.abc import A, B, C, D, E
from geometry_solver.easy_input import link, set_angle, get_angle, set_length, get_length, get_problem


def practical_test3():
    link(A, B, C, E)
    link(B, D)
    link(D, E)

    set_angle('ABD', 120)
    set_angle('BDE', 30)

    set_length('BD', 210)

    get_length('DE')
    
    # assert abs(result['answer'] - (3**(1/2) / 2) * 210) < 1e-3
    return get_problem()


if __name__ == '__main__':
    practical_test3()

