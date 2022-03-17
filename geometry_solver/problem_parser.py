
from geometry_solver.easy_input.abc import *
from geometry_solver.easy_input import *


def generate_code(code):
    print(code)
    exec(code)


class ProblemParser(object):
    
    def __init__(self):
        pass
    
    def parse(self, problem_file_path, encoding='utf8'):
        with open(problem_file_path, 'r', encoding=encoding) as f:
            for line in f:
                self._parse_line(line)
        return get_problem()
                
    def _parse_line(self, line):
        line = line.strip()
        if line == '' \
                or line.startswith('topology') \
                or line.startswith('preconditions') \
                or line.startswith('question'):
            return
        
        if line.startswith('link'):
            generate_code(line)
        elif line.startswith('('):
            self._parse_triplet(line)
        else:
            self._parse_target(line)

    def _parse_triplet(self, line):
        line = line[1:-1]
        triplet = [item.strip() for item in line.split(',')]
        if len(triplet) > 3:
            triplet = ', '.join(triplet[:-2]), triplet[-2], triplet[-1]
        sbj, obj, verb = triplet
        if verb == '=':
            self._process_equal(sbj, obj)
        elif verb.startswith('split'):
            self._process_split(sbj, obj, verb)
        elif verb == 'common_vertex':
            self._process_common_vertex(sbj, obj)
        elif verb == 'perpendicular':
            self._process_perpendicular(sbj, obj)
        elif verb == 'parallel':
            self._process_parallel(sbj, obj)
        elif verb == 'is':
            self._process_is(sbj, obj)

    def _parse_target(self, line):
        if line.startswith('angle'):
            angle = line.strip('angle_')
            generate_code("get_angle('{}')".format(angle))
        elif line.startswith('line'):
            line_ = line.strip('line_')
            generate_code("get_length('{}')".format(line_))
        elif line.startswith('circumference'):
            triangle = line.strip('circumference_')
            generate_code("get_circumference('{}')".format(triangle))
        elif line.startswith('area'):
            triangle = line.strip('area_')
            generate_code("get_area('{}')".format(triangle))
    
    def _process_equal(self, sbj, obj):
        if sbj.startswith('angle'):
            sbj = sbj.strip('angle_')
            if obj.startswith('angle'):
                obj = obj.strip('angle_')
                generate_code("angle_equivalence('{}', '{}')".format(sbj, obj))
            else:
                generate_code("set_angle('{}', {})".format(sbj, obj))
        elif sbj.startswith('line'):
            sbj = sbj.strip('line_')
            if obj.startswith('line'):
                obj = obj.strip('line_')
                generate_code("line_equivalence('{}', '{}')".format(sbj, obj))
            else:
                generate_code("set_length('{}', {})".format(sbj, obj))
                
    def _process_split(self, sbj, obj, verb):
        ratio_ind = verb.find('=')
        ratio = 0.5
        if ratio_ind != 1:
            ratio = float(verb.split('=')[1])
        
        if sbj.startswith('line'):
            sbj = sbj.strip('line_')
            obj = obj.strip('angle_')
            generate_code("split_angle('{}', '{}', ratio={})".format(obj, sbj, ratio))
        elif sbj.startswith('point'):
            sbj = sbj.strip('point_')
            obj = obj.strip('line_')
            generate_code("split_line('{}', '{}', ratio={})".format(obj, sbj, ratio))
            
    def _process_common_vertex(self, sbj, obj):
        sbj = sbj.strip()
        sbj = sbj[1:-1]
        around_points = ["'{}'".format(p.strip()) for p in sbj.split(',')]
        around_points_str = ', '.join(around_points)
        generate_code("common_vertex_angles('{}', [{}])".format(obj, around_points_str))
        
    def _process_perpendicular(self, sbj, obj):
        generate_code("perpendicular('{}', '{}')".format(sbj, obj))
    
    def _process_parallel(self, sbj, obj):
        generate_code("parallel('{}', '{}')".format(sbj, obj))
        
    def _process_is(self, sbj, obj):
        if obj == 'Equilateral_Triangle':
            generate_code("is_equilateral_triangle('{}')".format(sbj))
        elif obj == 'Right_Triangle':
            generate_code("is_right_triangle('{}', '{}')".format(sbj, sbj))

