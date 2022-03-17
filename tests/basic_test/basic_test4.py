from geometry_solver.entity import Entity, Point, Line, Angle, Triangle
from geometry_solver.condition import AttributeValue, RelationshipBased
from geometry_solver.relationship import SupplementaryAngle, Collineation
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
    
    entity = Entity('Basic test4')
    entity.add_entity(p_a, p_b, p_c, p_d)
    entity.add_entity(line_ac, line_bc, line_bd, line_cd)
    entity.add_entity(angle_acb, angle_acd)

    # Initialize conditions.
    conditions = []
    conditions.append(AttributeValue(angle_acb, angle=60))
    sa = SupplementaryAngle('ACB_ACD', angle1=angle_acb, angle2=angle_acd)
    col = Collineation('BCD', points=[p_b, p_c, p_d])
    conditions.append(RelationshipBased(sa))
    conditions.append(RelationshipBased(col))
    
    # Set target.
    target = Target(angle_acd, 'angle')
    
    return entity, target, conditions


def basic_test4():
    entity, target, conditions = get_problem()
    solver = Solver(entity=entity, target=target, conditions=conditions)
    solver.solve()


if __name__ == '__main__':
    basic_test4()

