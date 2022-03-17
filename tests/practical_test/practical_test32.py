from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, get_problem


def practical_test32():
    link(A, C)
    link(B, C)
    link(A, E, D, B)
    link(C, D)
    link(C, F ,E)
    link(D, F)
    
    set_angle('BAC', 40)
    set_angle('CBA', 72)

    split_angle('ACB', 'CE', 0.5)
    perpendicular('CD', 'AB')
    perpendicular('DF', 'CE')

    common_vertex_angles('C', ['A', 'E', 'D', 'B'])
    common_vertex_angles('D', ['A', 'F', 'C'])
    
    get_angle('CDF')
    
    # assert result['answer'] == 74
    return get_problem()
    

if __name__ == '__main__':
    practical_test32()    
