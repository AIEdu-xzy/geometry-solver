from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_angle, get_angle, get_problem


def practical_test1():
    link(A, D, B)
    link(A, E, C)
    link(D, F, C)
    link(B, F, E)
    link(B, C)

    set_angle('BAC', 45)
    set_angle('ABE', 40)
    set_angle('ACD', 20)

    get_angle('EFC')

    # assert result['answer'] == 75
    return get_problem()


if __name__ == '__main__':
    practical_test1()
