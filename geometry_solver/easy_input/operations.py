from geometry_solver.entity import Line, Angle, Triangle, Point
from geometry_solver.easy_input.parser import Parser
from geometry_solver.easy_input.helper import _get_target

parser = Parser()


# Problem setter.
def link(*points):
    """Link all points in one line."""
    parser.link(points)
    

def set_angle(angle_id, degree):
    """Set angle_id's angle degree."""
    parser.set_angle(angle_id, degree)
    

def set_length(line_id, length):
    """Set line_id's length."""
    parser.set_length(line_id, length)
    

def split_line(line_id, point_id, ratio=0.5):
    """Split a line with ratio `ratio`."""
    parser.add_line_split(line_id, point_id, ratio)


def split_angle(angle_id, line_id, ratio=0.5):
    """Split an angle with ratio `ratio`"""
    parser.add_angle_split(angle_id, line_id, ratio)
    

def parallel(*lines_id):
    """Set parallel, lines_id represents a list of line."""
    parser.add_parallel(lines_id)
    

def perpendicular(line1_id, line2_id):
    """Set perpendicular relationship between line1 and line2."""
    parser.add_perpendicular(line1_id, line2_id)
    

def common_vertex_angles(vertex_id, around_points):
    """Set common vertex angles relationship."""
    parser.add_common_vertex_angle(vertex_id, around_points)
    

def line_equivalence(obj_id1, obj_id2):
    parser.add_line_equivalent(obj_id1, obj_id2)

def angle_equivalence(obj_id1, obj_id2):
    parser.add_angle_equivalent(obj_id1, obj_id2)
    
def is_equilateral_triangle(triangle_id):
    parser.add_equilateral_triangle(triangle_id)

def is_right_triangle(triangle_id, right_angle_id):
    parser.add_right_triangle(triangle_id, right_angle_id)

# Target setter.
def get_length(line_id):
    """Get length of a line."""
    parser.set_target(line_id, Line, 'length')

    
def get_angle(angle_id):
    """Get angle of an angle."""
    parser.set_target(angle_id, Angle, 'angle')
    

def get_area(triangle_id):
    """Get area of an area."""
    parser.set_target(triangle_id, Triangle, 'area')
    

def get_circumference(triangle_id):
    """Get circumference of an area."""
    parser.set_target(triangle_id, Triangle, 'circumference')



def get_problem():
    """Paese problem for client"""
    problem = parser.parse_problem()
    parser.initialize()
    return problem
    
