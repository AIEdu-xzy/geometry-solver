from geometry_solver.entity import Angle, Entity, Line, Point, Triangle
from geometry_solver.relationship import Collineation, OppositeVerticalAngle,\
    SupplementaryAngle, CommonVertexAngle, NAngleSector, NLineSector, Perpendicular, Parallel, \
    ValueEquivalence, IsEquilateralTriangle, IsRightTriangle
from geometry_solver.condition import AttributeValue, RelationshipBased
from geometry_solver.target.target import Target
from geometry_solver.solver import Solver
from geometry_solver.problem import Problem


class Parser(object):
    
    
    def __init__(self, shown=False):
        self.initialize()
        self._shown = shown

    def initialize(self):
        self.problem = None
        entity = Entity('Entity container')
        self._points = set()
        self._lines = set()
        self._adj_table = {}
        self._angle_dict = {}
        self._line_dict = {}
        self._target_triplet = []
        self._line_alias = {}
        self._collineation_list = []
        self._common_vertex = []
        self._angle_split = []
        self._line_split = []
        self._perpendicular_pairs = []
        self._parallel_sets = []
        self._angle_equivalent = []
        self._line_equivalent = []
        self._equilateral_triangle = []
        self._right_triangle = []

    def link(self, points) -> Line:
        n = len(points)

        for p in points:
            self._points.add(p.id)
        
        if n >= 3:
            self._collineation_list.append([p.id for p in points])

        # Initialize line alias
        ends_str = points[0].id + points[-1].id
        for i in range(n):
            for j in range(i + 1, n):
                self._line_alias[points[i].id + points[j].id] = ends_str
                self._line_alias[points[j].id + points[i].id] = ends_str[::-1]

        for i in range(n):
            for j in range(i + 1, n):
                line_id = ''.join([points[i].id, points[j].id])
                self._lines.add(line_id)
        
        for p in points:
            if p.id not in self._adj_table:
                self._adj_table[p.id] = []
            for adj_p in points:
                if id(adj_p) == id(p):
                    continue
                self._adj_table[p.id].append(adj_p.id) 


    def parse_problem(self):
        """This function is used to generate entities automatically."""
        
        entity = Entity('Entity container')
        target = None
        conditions = []
        
        if self.problem is not None:
            return self.problem

        if self._shown:
            print('Using intelligent parser...')

        # Generate points.
        self.points = {pid: Point(pid) for pid in self._points}

        # Generate lines.
        self.lines = {}
        for lid in self._lines:
            lid = Parser._sort_string(lid)
            ends = [self.points[pid] for pid in lid]
            line = Line(lid, end1=ends[0], end2=ends[1])
            length = self._look_up_length(lid)
            if length is not None:
                cond = AttributeValue(line, length=length)
                conditions.append(cond)
            self.lines[lid] = line

        # Generate angles.
        self.angles = {}
        for vertex, adj_nodes in self._adj_table.items():
            n_adj = len(adj_nodes)
            for i in range(n_adj):
                for j in range(i + 1, n_adj):
                    node1, node2 = adj_nodes[i], adj_nodes[j]
                    node1 = self._line_alias[node1 + vertex][0]
                    node2 = self._line_alias[vertex + node2][1]
                    # Angle with zero degree
                    if node1 == node2:
                        continue
                    # Flat angle
                    if self._is_collineation(node1, vertex, node2):
                        continue
                    node1, node2 = sorted([node1, node2])
                    aid = ''.join([node1, vertex, node2])
                    line1 = self.find_line_by_ends(node1, vertex)
                    line2 = self.find_line_by_ends(node2, vertex)
                    sides = [line1, line2]
                    angle = Angle(aid, side1=sides[0], side2=sides[1], vertex=self.points[vertex])
                    self.angles[aid] = angle
                    degree = self._look_up_degree(aid)
                    if degree is not None:
                        cond = AttributeValue(angle, angle=degree)
                        conditions.append(cond)


        # Generate triangle.
        self.triangles = {}
        triangle_ids = self._analyse_triangle()
        for tid in triangle_ids:
            t_vertexes = [self.points[v] for v in tid]
            t_side1 = self.find_line_by_ends(tid[0], tid[1])
            t_side2 = self.find_line_by_ends(tid[1], tid[2])
            t_side3 = self.find_line_by_ends(tid[0], tid[2])
            t_sides = [t_side1, t_side2, t_side3]
            t_angle1 = self.find_angle_by_points(tid[0], tid[2], tid[1])
            t_angle2 = self.find_angle_by_points(tid[1], tid[0], tid[2])
            t_angle3 = self.find_angle_by_points(tid[0], tid[1], tid[2])
            t_angles = [t_angle1, t_angle2, t_angle3]
            triangle = Triangle(tid, 
                    vertex1=t_vertexes[0],
                    vertex2=t_vertexes[1],
                    vertex3=t_vertexes[2],
                    side1=t_sides[0],
                    side2=t_sides[1],
                    side3=t_sides[2],
                    angle1=t_angles[0],
                    angle2=t_angles[1],
                    angle3=t_angles[2])
            self.triangles[tid] = triangle

        if self._shown:
            print('points: ', sorted(self.points.keys()))
            print('lines', sorted(self.lines.keys()))
            print('angles: ', sorted(self.angles.keys()))
            print('triangles: ', sorted(self.triangles.keys()))


        # Generate relationships.
        collineations = {}
        for col in self._collineation_list:
            col_id = 'Collineation ' + ''.join([p for p in col])
            ps = [self.points[pid] for pid in col]
            r = Collineation(col_id, points=ps)
            collineations[col_id] = r


        # Generate opposite vertival angles.
        opposite_angles = {}
        n_cols = len(self._collineation_list)
        for i in range(n_cols):
            for j in range(i + 1, n_cols):
                col1 = self._collineation_list[i]
                col2 = self._collineation_list[j]
                common = list(set(col1) & set(col2))
                if len(common) != 1:
                    continue
                vertex = common[0]
                if vertex in [col1[0], col1[-1], col2[0], col2[-1]]:
                    continue

                angle1_1 = self.find_angle_by_points(col1[0], vertex, col2[0])
                angle1_2 = self.find_angle_by_points(col1[-1], vertex, col2[-1])
                rid = ' '.join(['OppositeAngle', angle1_1.id, angle1_2.id])
                opposite_angles[rid] = OppositeVerticalAngle(rid, 
                    angle1=angle1_1, angle2=angle1_2, vertex=vertex)

                angle2_1 = self.find_angle_by_points(col1[0], vertex, col2[-1])
                angle2_2 = self.find_angle_by_points(col1[-1], vertex, col2[0])
                rid = ' '.join(['OppositeAngle', angle2_1.id, angle2_2.id])
                opposite_angles[rid] = OppositeVerticalAngle(rid, 
                    angle1=angle2_1, angle2=angle2_2, vertex=vertex)


        # Generate supplementary angles.
        supplementary_angles = {}
        for col in self._collineation_list:
            for p in col[1:-1]:
                for adj_p in self._adj_table[p]:
                    if adj_p in col:
                        continue
                    angle1 = self.find_angle_by_points(col[0], p, adj_p)
                    angle2 = self.find_angle_by_points(col[-1], p, adj_p)
                    rid = ' '.join(['SupplementaryAngle', angle1.id, angle2.id])
                    supplementary_angles[rid] = \
                        SupplementaryAngle(rid, angle1=angle1, angle2=angle2)

        
        # Generate common vertex angles.
        common_vertex_angles = {}
        for v, arounds in self._common_vertex:
            vertex = self.points[v]
            ends = [self.points[pid] for pid in arounds]
            rid = ' '.join(['CommonVertexAngle', v, ''.join(arounds)])
            r = CommonVertexAngle(rid, vertex=vertex, ends=ends)
            common_vertex_angles[rid] = r

        
        # Generate n angles sector.
        n_angles_sector = {}
        for aid, lid, ratio in self._angle_split:
            near_line = self.find_line_by_ends(*aid[:2])
            angle_ = self.find_angle_by_points(*aid)
            line_ = self.find_line_by_ends(*lid)
            rid = ' '.join([angle_.id, line_.id, str(ratio), near_line.id])
            r = NAngleSector(rid, angle=angle_, split_line=line_, near_line=near_line)
            cond = AttributeValue(r, ratio=ratio)
            conditions.append(cond)
            n_angles_sector[rid] = r


        # Generate n line sector.
        n_line_sector = {}
        for lid, pid, ratio in self._line_split:
            rid = ' '.join(['NLineSector', lid, pid, str(ratio)])
            r = NLineSector(rid, 
                            line=self.find_line_by_ends(*lid), 
                            split_point=self.points[pid], 
                            near_point=self.points[lid[0]])
            cond = AttributeValue(r, ratio=ratio)
            conditions.append(cond)
            n_line_sector[rid] = r


        # Generate perpendicular relationship.
        perpendiculars = {}
        for lid1, lid2 in self._perpendicular_pairs:
            rid = ' '.join(['Perpendicular', lid1, lid2])
            r = Perpendicular(rid,
                              line1=self.find_line_by_ends(*lid1),
                              line2=self.find_line_by_ends(*lid2),
                              foot_point=None)
            perpendiculars[rid] = r

        # Generate parallel relationship.
        parallels = {}
        for line_ids_tp in self._parallel_sets:
            line_ids = list(line_ids_tp)
            line_num = len(line_ids)
            for i in range(line_num):
                for j in range(i + 1, line_num):
                    reverse = False
                    if line_ids[i][0] > line_ids[i][1]:
                        reverse = not reverse
                        line_ids[i] = line_ids[i][::-1]
                    if line_ids[j][0] > line_ids[j][1]:
                        reverse = not reverse
                        line_ids[j] = line_ids[j][::-1]
                    line1 = self.lines[line_ids[i]]
                    line2 = self.lines[line_ids[j]]
                    rid = ' '.join(['Parallel', line_ids[i], line_ids[j]])
                    parallels[rid] = Parallel(rid, line1, line2, reverse=reverse)
        
        # Generate ValueEquivalence relationship.
        value_equivalence = {}
        for obj_list in self._angle_equivalent:
            obj_list = [self.find_angle_by_points(*obj_id) for obj_id in obj_list]
            rid = '='.join([obj.id for obj in obj_list])
            r = ValueEquivalence(rid, obj_list=obj_list, attr_list=['angle']*len(obj_list))
            value_equivalence[rid] = r
        for obj_list in self._line_equivalent:
            obj_list = [self.find_line_by_ends(*obj_id) for obj_id in obj_list]
            rid = '='.join([obj.id for obj in obj_list])
            r = ValueEquivalence(rid, obj_list=obj_list, attr_list=['length']*len(obj_list))
            value_equivalence[rid] = r
            
        # Generate equilateral triangle
        equilateral_triangles = {}
        for th_id in self._equilateral_triangle:
            std_th_id = ''.join(sorted(th_id))
            th = self.triangles[std_th_id]
            r = IsEquilateralTriangle(std_th_id, th)
            equilateral_triangles[std_th_id] = r
            
        # Generate right triangle
        right_triangles = {}
        for th_id, aid in self._right_triangle:
            std_th_id = ''.join(sorted(th_id))
            right_angle = self.find_angle_by_points(*aid)
            th = self.triangles[std_th_id]
            r = IsRightTriangle(std_th_id, th, right_angle)
            right_triangles[std_th_id] = r

        if self._shown:
            print('collineations: ', sorted(collineations.keys()))
            print('opposite angles: ', sorted(opposite_angles.keys()))
            print('supplementary angles: ', sorted(supplementary_angles.keys()))
            print('common vertex angles: ', sorted(common_vertex_angles.keys()))
            print('n angles sector: ', sorted(n_angles_sector.keys()))
            print('n line sector: ', sorted(n_line_sector.keys()))
            print('perpendiculars: ', sorted(perpendiculars.keys()))
            print('parallels: ', sorted(parallels.keys()))

        relationships = []
        relationships += collineations.values()
        relationships += opposite_angles.values()
        relationships += supplementary_angles.values()
        relationships += common_vertex_angles.values()
        relationships += n_angles_sector.values()
        relationships += perpendiculars.values()
        relationships += n_line_sector.values()
        relationships += parallels.values()
        relationships += value_equivalence.values()
        relationships += equilateral_triangles.values()
        relationships += right_triangles.values()
        for r in relationships:
            conditions.append(RelationshipBased(r))

        entity.add_entity(*(self.points.values()))
        entity.add_entity(*(self.lines.values()))
        entity.add_entity(*(self.angles.values()))
        entity.add_entity(*(self.triangles.values()))

        # Generate target.
        if self._target_triplet is None:
            raise NotImplementedError("Target not setted.")
        target_id = self._target_triplet[0]
        target_type = self._target_triplet[1]
        target_attr = self._target_triplet[2]
        target_obj = entity.find_child(target_id, target_type)
        target = Target(target_obj, target_attr)

        problem = Problem(entity, conditions, target)
        return problem

    def execute(self):
        problem = self.parse_problem()
        solver = Solver(problem)
        result = solver.solve()
        return result

    def _is_collineation(self, *points):
        if len(points) < 3:
            return True
        for col in self._collineation_list:
            on_a_line = True
            for p in points:
                if p not in col:
                    on_a_line = False
                    break
            if on_a_line:
                return True
        return False


    def _extend_angle(self, pid1, vertex, pid2):
        pid1 = self._line_alias[pid1 + vertex][0]
        pid2 = self._line_alias[vertex + pid2][1]
        if pid1 > pid2:
            pid1, pid2 = pid2, pid1
        return ''.join([pid1, vertex, pid2])


    def _retrieve_angle(self, angle_id):
        pid1, vertex, pid2 = angle_id
        pid1, pid2 = sorted([pid1, pid2])
        aid = self._extend_angle(pid1, vertex, pid2)
        return aid


    def _analyse_triangle(self):
        all_triangles = set()
        for p in self._adj_table.keys():
            self._dfs_triangle([p], all_triangles)
        return {t for t in all_triangles if not self._is_collineation(*t)}


    def _dfs_triangle(self, trajectory, all_triangles):
        if len(trajectory) == 4:
            if trajectory[0] == trajectory[-1]:
                triangle_id = ''.join(sorted(trajectory[:3]))
                all_triangles.add(triangle_id)
            return
        node = trajectory[-1]
        for adj_node in self._adj_table[node]:
            if len(trajectory) < 3 and adj_node in trajectory:
                continue
            self._dfs_triangle(trajectory + [adj_node], all_triangles)


    def set_angle(self, angle_id, degree):
        aid = self._retrieve_angle(angle_id)
        self._angle_dict[aid] = degree


    def set_length(self, line_id, length):
        line_id = ''.join(sorted(line_id))
        self._line_dict[line_id] = length


    def _look_up_degree(self, aid):
        return self._loop_up(aid, self._angle_dict)

    def _look_up_length(self, lid):
        return self._loop_up(lid, self._line_dict)

    def _loop_up(self, id_, dict_):
        if id_ not in dict_:
            return None
        return dict_[id_]

    def _type_id_transfer(self, id_, type_):
        new_id = ''
        if type_ == Line:
            new_id = ''.join(sorted(id_))
        elif type_ == Angle:
            new_id = self._retrieve_angle(id_)
        elif type_ == Triangle:
            new_id = ''.join(sorted(id_))
        return new_id

    def set_target(self, id_, type_, attr):
        id_ = self._type_id_transfer(id_, type_)
        # self._target_triplet.append((id_, type_, attr))
        # Currently only one target solver is supported.
        self._target_triplet = [id_, type_, attr]

    def add_common_vertex_angle(self, vertex_id, around_points):
        self._common_vertex.append((vertex_id, around_points))


    def add_angle_split(self, angle_id, line_id, ratio):
        self._angle_split.append((angle_id, line_id, ratio))


    def add_line_split(self, line_id, point_id, ratio):
        self._line_split.append((line_id, point_id, ratio))

    
    def add_perpendicular(self, line_id1, line_id2):
        self._perpendicular_pairs.append((line_id1, line_id2))

    def add_parallel(self, line_ids):
        self._parallel_sets.append(line_ids)
        
    def _add_value_equivalent(self, obj_id1, obj_id2, value_record):
        # value_record contains a list of (obj_list)
        duplicate = False
        for obj_list in value_record:
            if obj_id1 in obj_list:
                obj_list.append(obj_id2)
                duplicate = True
                break
            elif obj_id2 in obj_list:
                obj_list.append(obj_id1)
                duplicate = True
                break
        if not duplicate:
           value_record.append(tuple([obj_id1, obj_id2]))
        
    def add_angle_equivalent(self, obj_id1, obj_id2):
        self._add_value_equivalent(obj_id1, obj_id2, self._angle_equivalent)
           
    def add_line_equivalent(self, obj_id1, obj_id2):
        self._add_value_equivalent(obj_id1, obj_id2, self._line_equivalent)
        
    def add_equilateral_triangle(self, triangle_id):
        self._equilateral_triangle.append(triangle_id)
        
    def add_right_triangle(self, triangle_id, right_angle_id):
        self._right_triangle.append((triangle_id, right_angle_id))

    def find_line_by_ends(self, pid1, pid2):
        return self.lines[Parser._sort_string(''.join([pid1, pid2]))]
    
    def find_angle_by_points(self, pid1, vertex, pid2):
        return self.angles[self._extend_angle(pid1, vertex, pid2)]

    def _sort_string(str_):
        return ''.join(sorted(str_))
    
    