from geometry_solver.entity import Entity, Point, Line, Angle, Triangle
from geometry_solver.relationship import Collineation
from geometry_solver.condition import AttributeValue, RelationshipBased
from geometry_solver import Target, Solver


def get_problem():
    """Test for line sum."""
    # Initialize problem structure.
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')

    line_ab = Line('AB', end1=p_a, end2=p_b)
    line_bc = Line('BC', end1=p_b, end2=p_c)
    line_ac = Line('AC', end1=p_a, end2=p_c)

    entity = Entity('Basic test1')
    entity.add_entity(p_a, p_b, p_c)
    entity.add_entity(line_ab, line_bc, line_ac)

    # Set target.
    target = Target(line_bc, 'length')

    # Initialize conditions.
    conditions = []
    conditions.append(AttributeValue(line_ab, length=2))
    conditions.append(AttributeValue(line_ac, length=5))
    col = Collineation('ABC', [p_a, p_b, p_c])
    r = RelationshipBased(col)
    conditions.append(r)
    
    return entity, target, conditions


def basic_test1():
    entity, target, conditions = get_problem()
    solver = Solver(entity=entity, target=target, conditions=conditions)
    solver.solve()


if __name__ == '__main__':
    basic_test1()

