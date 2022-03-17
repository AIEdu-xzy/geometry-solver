from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_angle, get_angle, get_problem


def basic_test25():
    link(A, B)
    link(A, C)
    link(B, C)

    set_angle('BAC', 45)

    get_angle('ABC')

    # assert result['answer'] == 75
    return get_problem()


if __name__ == '__main__':
    basic_test25()
