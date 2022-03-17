from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_angle, get_angle, get_problem, angle_equivalence


def practical_test131():
    link(A, B, C)
    link(B, D)

    set_angle('ABD', 70)

    get_angle('CBD')

    # assert result['answer'] == 75
    return get_problem()


if __name__ == '__main__':
    practical_test131()
