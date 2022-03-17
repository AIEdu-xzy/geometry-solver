from geometry_solver.entity import Entity, Point, Line, Angle, Triangle
from geometry_solver.condition import AttributeValue, RelationshipBased
from geometry_solver.relationship import CommonVertexAngle
from geometry_solver import Target, Solver


def get_problem():
    # Initialize problem structure.
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')

    line_ab = Line('AB', end1=p_a, end2=p_b)
    line_ac = Line('AC', end1=p_a, end2=p_c)
    line_ad = Line('AD', end1=p_a, end2=p_d)

    angle_bac = Angle('BAC', side1=line_ab, side2=line_ac, vertex=p_a)
    angle_cad = Angle('CAD', side1=line_ac, side2=line_ad, vertex=p_a)
    angle_bad = Angle('BAD', side1=line_ab, side2=line_ad, vertex=p_a)
    
    entity = Entity('Basic test3')
    entity.add_entity(p_a, p_b, p_c, p_d)
    entity.add_entity(line_ab, line_ac, line_ad)
    entity.add_entity(angle_bac, angle_bad, angle_cad)

    # Initialize conditions.
    conditions = []
    conditions.append(AttributeValue(angle_bac, angle=60))
    conditions.append(AttributeValue(angle_cad, angle=30))
    cva = CommonVertexAngle('A_BCD', vertex=p_a, ends=[p_b, p_c, p_d])
    r = RelationshipBased(cva)
    conditions.append(r)
    
    # Set target.
    target = Target(angle_bad, 'angle')
    
    return entity, target, conditions


def basic_test3():
    entity, target, conditions = get_problem()
    solver = Solver(entity=entity, target=target, conditions=conditions)
    solver.solve()


if __name__ == '__main__':
    basic_test3()

