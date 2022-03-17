from geometry_solver.entity import Entity, Point, Line, Angle, Triangle
from geometry_solver.condition import AttributeValue, RelationshipBased
from geometry_solver.relationship import SimilarTriangle
from geometry_solver.indexer.indexer import Indexer
from geometry_solver.graph.deduction_graph import DeductionGraph
from geometry_solver.pattern import TrianglePattern, AttributeState
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

    triangle_abc = Triangle(
            'ABC', 
            vertex1=p_c, vertex2=p_a, vertex3=p_b,
            side1=line_ab, side2=line_bc, side3=line_ac,
            angle1=angle_c, angle2=angle_a, angle3=angle_b)
    
    p_d = Point('D')
    p_e = Point('E')
    p_f = Point('F')

    line_de = Line('DE', end1=p_d, end2=p_e)
    line_ef = Line('EF', end1=p_e, end2=p_f)
    line_df = Line('DF', end1=p_d, end2=p_f)

    angle_d = Angle('EDF', side1=line_de, side2=line_df, vertex=p_d)
    angle_e = Angle('DEF', side1=line_de, side2=line_ef, vertex=p_e)
    angle_f = Angle('DFE', side1=line_df, side2=line_ef, vertex=p_f)

    triangle_def = Triangle(
            'DEF', 
            vertex1=p_f, vertex2=p_d, vertex3=p_e,
            side1=line_de, side2=line_ef, side3=line_df,
            angle1=angle_f, angle2=angle_d, angle3=angle_e)

    entity = Entity('Basic test19')
    entity.add_entity(triangle_abc)
    entity.add_entity(triangle_def)

    # Set target.
    target = Target(line_df, 'length')

    # Initialize conditions.
    conditions = []
    conditions.append(AttributeValue(angle_a, angle=60))
    conditions.append(AttributeValue(angle_b, angle=90))
    conditions.append(AttributeValue(angle_c, angle=30))
    conditions.append(AttributeValue(angle_d, angle=60))
    conditions.append(AttributeValue(angle_e, angle=90))
    conditions.append(AttributeValue(angle_f, angle=30))
    conditions.append(AttributeValue(line_ab, length=1))
    conditions.append(AttributeValue(line_ac, length=2))
    conditions.append(AttributeValue(line_de, length=1))
    return entity, target, conditions


def basic_pattern():
    entity, target, conditions = get_problem()
    
    graph = DeductionGraph(conditions, target)
    indexer = Indexer(entity, graph)
    pattern = TrianglePattern(angle_A=AttributeState.KNOWN,
                              angle_B=AttributeState.KNOWN,
                              angle_C=AttributeState.KNOWN)
    conditions, entitis = indexer.index_by_pattern(pattern, True)
    print(entitis)
    print(conditions)

if __name__ == '__main__':
    basic_pattern()

