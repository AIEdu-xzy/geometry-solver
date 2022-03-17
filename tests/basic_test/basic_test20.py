from geometry_solver.entity import Entity, Point, Line, Angle, Triangle
from geometry_solver.condition import AttributeValue, RelationshipBased
from geometry_solver import Target, Solver
from geometry_solver.relationship import NAngleSector


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
    angle_bad = Angle('BAD', side1=line_ab, side2=line_ad, vertex=p_a)
    angle_cad = Angle('CAD', side1=line_ac, side2=line_ad, vertex=p_a)

    entity = Entity('Basic test20')
    entity.add_entity(p_a, p_b, p_c, p_d)
    entity.add_entity(line_ab, line_ac, line_ad)
    entity.add_entity(angle_bac, angle_bad, angle_cad)

    # Set target.
    target = Target(angle_bad, 'angle')

    # Initialize conditions.
    conditions = []
    conditions.append(AttributeValue(angle_bac, angle=30))
    r = NAngleSector('BAD_AC', angle=angle_bad, split_line=line_ac, near_line=line_ab)
    conditions.append(RelationshipBased(r))
    conditions.append(AttributeValue(r, ratio=0.25))
    return entity, target, conditions


def basic_test20():
    entity, target, conditions = get_problem()
    solver = Solver(entity=entity, target=target, conditions=conditions)
    solver.solve()


if __name__ == '__main__':
    basic_test20()

