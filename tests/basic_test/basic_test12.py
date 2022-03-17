from geometry_solver.entity import Entity, Point, Line, Angle, Triangle
from geometry_solver.relationship import Parallel, Collineation
from geometry_solver.condition import AttributeValue, RelationshipBased
from geometry_solver import Target, Solver


def get_problem():
    """Test for line sum."""
    # Initialize problem structure.
    p_a = Point('A')
    p_b = Point('B')
    p_c = Point('C')
    p_d = Point('D')
    p_e = Point('E')
    p_f = Point('F')
    p_g = Point('G')
    p_h = Point('H')

    line_ab = Line('AB', end1=p_a, end2=p_b)
    line_af = Line('AF', end1=p_a, end2=p_f)
    line_bf = Line('BF', end1=p_b, end2=p_f)
    line_cd = Line('CD', end1=p_c, end2=p_d)
    line_cg = Line('CG', end1=p_c, end2=p_g)
    line_dg = Line('DG', end1=p_d, end2=p_g)
    line_ef = Line('EF', end1=p_e, end2=p_f)
    line_eg = Line('EG', end1=p_e, end2=p_g)
    line_eh = Line('EH', end1=p_e, end2=p_h)
    line_fg = Line('FG', end1=p_f, end2=p_g)
    line_fh = Line('FH', end1=p_f, end2=p_h)
    line_gh = Line('GH', end1=p_g, end2=p_h)
    
    angle_afe = Angle('AFE', side1=line_af, side2=line_ef, vertex=p_f)
    angle_bfe = Angle('BFE', side1=line_bf, side2=line_ef, vertex=p_f)
    angle_afh = Angle('AFH', side1=line_af, side2=line_fh, vertex=p_f)
    angle_bfh = Angle('BFH', side1=line_bf, side2=line_fh, vertex=p_f)
    angle_cgh = Angle('CGH', side1=line_cg, side2=line_gh, vertex=p_g)
    angle_dgh = Angle('DGH', side1=line_dg, side2=line_gh, vertex=p_g)
    angle_cge = Angle('CGE', side1=line_cg, side2=line_eg, vertex=p_g)
    angle_dge = Angle('DGE', side1=line_dg, side2=line_eg, vertex=p_g)

    entity = Entity('Basic test12')
    for name, obj in locals().items():
        if name.startswith(tuple(['p_', 'line_', 'angle_'])):
            entity.add_entity(obj)

    # Initialize conditions.
    conditions = []
    conditions.append(AttributeValue(angle_bfe, angle=60))
    parallel = Parallel('AB_CD', line1=line_ab, line2=line_cd)
    r = RelationshipBased(parallel)
    conditions.append(r)
    conditions.append(RelationshipBased(Collineation('AFB', points=[p_a, p_f, p_b])))
    conditions.append(RelationshipBased(Collineation('CGD', points=[p_c, p_g, p_d])))
    conditions.append(RelationshipBased(Collineation('EFGH', points=[p_e, p_f, p_g, p_h])))
    
    # Set target.
    target = Target(angle_dge, 'angle')
    
    return entity, target, conditions


def basic_test12():
    entity, target, conditions = get_problem()
    solver = Solver(entity=entity, target=target, conditions=conditions)
    solver.solve()


if __name__ == '__main__':
    basic_test12()

