from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_angle, get_angle, get_problem


def practical_test2():
    link(A, D)
    link(A, B)
    link(A, E, C)
    link(B, E, D)
    link(B, C)

    set_angle('BAC', 60)
    set_angle('ACB', 30)
    set_angle('ADB', 45)
    set_angle('ABD', 45)
    set_angle('BAD', 90)
    set_angle('ABC', 90)
    
    get_angle('AEB')

    # assert result['answer'] == 75
    return get_problem()


if __name__ == '__main__':
    practical_test2()

