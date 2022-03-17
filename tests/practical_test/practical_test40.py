from geometry_solver.easy_input.abc import A, B, C, D, E, F
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, angle_equivalence, get_problem



# problem idx in another docx:44
def practical_test40():
    link(A, B)
    link(A, D)
    link(B, C)
    link(C, D)
    link(A, C)
    link(B, D)

    common_vertex_angles('A', ['B', 'C', 'D'])
    common_vertex_angles('B', ['A', 'D', 'C'])
    common_vertex_angles('C', ['B', 'A', 'D'])
    common_vertex_angles('D', ['A', 'B', 'C'])

    set_angle('BAD', 60)
    set_angle('BCD', 120)
    set_length('BC', 5)
    set_length('DC', 3)
    
    angle_equivalence('ABD', 'ADB')
    
    get_length('AC')
    
    # assert result['answer'] == 8
    return get_problem()
    

if __name__ == '__main__':
    practical_test40()
    
    