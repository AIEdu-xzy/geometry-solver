from geometry_solver.entity import Entity, Point, Line, Angle, Triangle
from geometry_solver.condition import AttributeValue, RelationshipBased
from geometry_solver.relationship import Perpendicular, Collineation
from geometry_solver import Target, Solver


def get_problem():
    # Initialize problem structure.
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')

    line_ac = Line('AC', end1=p_a, end2=p_c)
    line_bc = Line('BC', end1=p_b, end2=p_c)
    line_bd = Line('BD', end1=p_b, end2=p_d)
    line_cd = Line('CD', end1=p_c, end2=p_d)

    angle_acb = Angle('ACB', side1=line_ac, side2=line_bc, vertex=p_c)
    angle_acd = Angle('ACD', side1=line_ac, side2=line_cd, vertex=p_c)
    
    entity = Entity('Basic test5')
    entity.add_entity(p_a, p_b, p_c, p_d)
    entity.add_entity(line_ac, line_bc, line_bd, line_cd)
    entity.add_entity(angle_acb, angle_acd)

    # Initialize conditions.
    conditions = []
    p = Perpendicular('AC_BD', line1=line_ac, line2=line_bd, foot_point=p_c)
    conditions.append(RelationshipBased(p))

    # Set target.
    target = Target(angle_acd, 'angle')

    return entity, target, conditions


def basic_test5():
    entity, target, conditions = get_problem()
    solver = Solver(entity=entity, target=target, conditions=conditions)
    solver.solve()


if __name__ == '__main__':
    basic_test5()

