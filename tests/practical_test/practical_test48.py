from geometry_solver.easy_input.abc import A, B, C, D, E, G
from geometry_solver.easy_input import link, set_length, set_angle, split_angle, perpendicular, get_angle, common_vertex_angles, get_angle, get_length, split_line, get_problem



def practical_test48():
    link(A, G, E)
    link(A, D, C)
    link(B, G, D)
    link(B, E, C)

    perpendicular('AC', 'CB')
    split_line('AC', 'D')
    split_line('BC', 'E')
    set_length('CD', 15)
    set_length('CE', 15)

    get_length('BD')

    # assert result['answer'] == 33.5
    return get_problem()
    
    
if __name__ == '__main__':
    practical_test48()
    
    