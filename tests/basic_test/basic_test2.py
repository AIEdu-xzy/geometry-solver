from geometry_solver.entity import Entity, Point, Line, Angle, Triangle
from geometry_solver.condition import AttributeValue
from geometry_solver import Target, Solver


def get_problem():
    # Initialize problem structure.
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')

    line_ab = Line('AB', end1=p_a, end2=p_b)
    line_bc = Line('BC', end1=p_b, end2=p_c)
    line_ac = Line('AC', end1=p_a, end2=p_c)

    angle_a = Angle('BAC', side1=line_ab, side2=line_ac, vertex=p_a)
    angle_b = Angle('ABC', side1=line_ab, side2=line_bc, vertex=p_b)
    angle_c = Angle('ACB', side1=line_ac, side2=line_bc, vertex=p_c)

    triangle = Triangle(
            'ABC', 
            vertex1=p_c, vertex2=p_a, vertex3=p_b,
            side1=line_ab, side2=line_bc, side3=line_ac,
            angle1=angle_c, angle2=angle_a, angle3=angle_b)
    
    entity = Entity('Basic test2')
    entity.add_entity(triangle)

    # Set target.
    target = Target(angle_c, 'angle')

    # Initialize conditions.
    conditions = []
    conditions.append(AttributeValue(angle_a, angle=60))
    conditions.append(AttributeValue(angle_b, angle=30))
    
    return entity, target, conditions


def basic_test2():
    entity, target, conditions = get_problem()
    solver = Solver(entity=entity, target=target, conditions=conditions)
    solver.solve()


if __name__ == '__main__':
    basic_test2()

