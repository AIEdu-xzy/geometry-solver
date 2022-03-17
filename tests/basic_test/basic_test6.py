from geometry_solver.entity import Entity, Point, Line, Angle, Triangle
from geometry_solver.condition import AttributeValue, RelationshipBased
from geometry_solver.relationship import OppositeVerticalAngle, Collineation
from geometry_solver import Target, Solver


def get_problem():
    """Test for equality of opposite vertical angle."""
    # Initialize problem structure.
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')
    p_o = Point('O')

    line_ao = Line('AO', end1=p_a, end2=p_o)
    line_ad = Line('AD', end1=p_a, end2=p_d)
    line_do = Line('DO', end1=p_d, end2=p_o)
    line_bo = Line('BO', end1=p_b, end2=p_o)
    line_bc = Line('BC', end1=p_b, end2=p_c)
    line_co = Line('CO', end1=p_c, end2=p_o)

    angle_aob = Angle('AOB', side1=line_ao, side2=line_bo, vertex=p_o)
    angle_aoc = Angle('AOC', side1=line_ao, side2=line_co, vertex=p_o)
    angle_cod = Angle('COD', side1=line_co, side2=line_do, vertex=p_o)
    angle_bod = Angle('BOD', side1=line_bo, side2=line_do, vertex=p_o)
    
    entity = Entity('Basic test6')
    entity.add_entity(p_a, p_b, p_c, p_d, p_o)
    entity.add_entity(line_ao, line_ad, line_do, line_bo, line_bc, line_co)
    entity.add_entity(angle_aob, angle_aoc, angle_cod, angle_bod)

    # Initialize conditions.
    conditions = []
    ova1 = OppositeVerticalAngle('AOB_COD', angle1=angle_aob, angle2=angle_cod, vertex=p_o)
    ova2 = OppositeVerticalAngle('AOC_BOD', angle1=angle_aoc, angle2=angle_bod, vertex=p_o)
    conditions.append(RelationshipBased(ova1))
    conditions.append(RelationshipBased(ova2))
    conditions.append(AttributeValue(angle_aob, angle=60))

    # Set target.
    target = Target(angle_cod, 'angle')

    return entity, target, conditions


def basic_test6():
    entity, target, conditions = get_problem()
    solver = Solver(entity=entity, target=target, conditions=conditions)
    solver.solve()


if __name__ == '__main__':
    basic_test6()

