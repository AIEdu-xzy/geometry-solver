from geometry_solver.entity import Entity, Point, Line, Angle, Triangle
from geometry_solver.condition import AttributeValue, RelationshipBased
from geometry_solver import Target, Solver
from geometry_solver.relationship import NLineSector


def get_problem():
    # Initialize problem structure.
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')

    line_ab = Line('AB', end1=p_a, end2=p_b)
    line_ac = Line('AC', end1=p_a, end2=p_c)
    line_bc = Line('BC', end1=p_b, end2=p_c)

    entity = Entity('Basic test21')
    entity.add_entity(line_ab, line_ac, line_bc)

    # Set target.
    target = Target(line_ac, 'length')

    # Initialize conditions.
    conditions = []
    conditions.append(AttributeValue(line_ab, length=1))
    r = NLineSector('AC_B', line=line_ac, split_point=p_b, nearer_point=p_a)
    conditions.append(RelationshipBased(r))
    conditions.append(AttributeValue(r, ratio=0.5))
    
    return entity, target, conditions


def basic_test21():
    entity, target, conditions = get_problem()
    solver = Solver(entity=entity, target=target, conditions=conditions)
    solver.solve()


if __name__ == '__main__':
    basic_test21()

