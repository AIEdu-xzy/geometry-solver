from typing import List, Union

from geometry_solver.indexer.base_indexer import BaseIndexer
from geometry_solver.entity import Entity, Triangle, Angle, Line, Triangle
from geometry_solver.pattern.pattern import Pattern
from geometry_solver.condition import Condition, AttributeValue
from geometry_solver.graph.deduction_graph import DeductionGraph
from geometry_solver.condition.attribute_value import AttributeValue
from geometry_solver.pattern.triangle_pattern import TrianglePattern
from geometry_solver.pattern.attribute_state import AttributeState


class PatternIndexer(BaseIndexer):
    
    def __init__(self,
            entity: Entity, 
            graph: DeductionGraph):
        self.dispatch_map = {
            Angle: self._extract_angle_pattern,
            Line: self._extract_line_pattern,
            Triangle: self._extract_triangle_pattern,
        }
        self.build_index(entity, graph)

    def build_index(self,
            entity: Entity, 
            graph: DeductionGraph):
        self.entity = entity
        self.graph = graph
        # Pattern is not hashable, so list is required.
        # triangle_pattern_table is a list of tuple:
        # (pattern, entities, value pattern)
        self.triangle_pattern_table = []
        for e in entity.children:
            if type(e) in self.dispatch_map.keys():
                # Extract pattern from entity.
                self._extract_from_entity(e)
    
    def _extract_from_entity(self, entity):
        """"Extract pattern from entity and store in table."""
        for p, vp in self._extract_pattern(entity):
            found = False
            for pt, entities, vp_list in self.triangle_pattern_table:
                if p == pt:
                    found = True
                    duplicate = False
                    for e in entities:
                        if e == entity:
                            duplicate = True
                            break
                    if not duplicate:
                        vp_list.append(vp)
                        entities.append(entity)
                    break
            if not found:
                self.triangle_pattern_table.append((p, [entity], [vp]))

    def update_index(self, new_obj: Union[Condition, Entity], indexer):
        if type(new_obj) == AttributeValue:
            self._update_index(new_obj, indexer)

    def _update_index(self, cond: AttributeValue, indexer):
        ths = indexer.index_by_ownership(cond.obj, Triangle)
        new_table = []
        # Delete updated triangle.
        for pt, e_list, vp_list in self.triangle_pattern_table:
            new_e_list = []
            new_vp_list = []
            for i in range(len(e_list)):
                e = e_list[i]
                vp = vp_list[i]
                if e not in ths:
                    new_e_list.append(e)
                    new_vp_list.append(vp)
            new_table.append((pt, new_e_list, new_vp_list))
                    
        self.triangle_pattern_table = new_table
        for th in ths:
            self._extract_from_entity(th)
    
    def index(self, pattern: Pattern):
        """Return a list of modified pattern whose UNKOWN attributes 
            are replaced by AttributeValue condition.
            And corresponding entity.
        """
        
        def intersection(s1, s2):
            for e in s2:
                if e not in s1:
                    s1.append(e)
        
        all_entity = []
        all_vp = []
        for p, entity_list, vp_list in self.triangle_pattern_table:
            if pattern == p:
                intersection(all_entity, entity_list)
                intersection(all_vp, vp_list)
        return all_vp, all_entity
    
    def _extract_pattern(self, entity: Entity):
        """This method is responsible for dispatch pattern extraction 
        according to type of entity.
        
        Return a tuple of (pattern, (known_conditions, unknown_conditions)).
        """
        return self.dispatch_map[type(entity)](entity)
    
    def _extract_triangle_pattern(self, triangle: Triangle):
        """Extract patterns of triangle.
        
        Return a list of (pattern, (known_conditions, unknown_conditions)).
        """
        ret = []
        pattern_list = []
        value_pattern_list = []
        
        attr_map = {
            Angle: 'angle',
            Line: 'length'
        }
        
        value_conds = self.graph.attr_value_conds
        
        def find_obj(obj, attr=None):
            for c in value_conds:
                if c.obj == obj:
                    if attr is None or attr == c.attr_name:
                        return c
            if attr is None:
                attr = attr_map[type(obj)]
            return AttributeValue(obj, **{attr: None})
        
        angle1 = find_obj(triangle.angle1)
        angle2 = find_obj(triangle.angle2)
        angle3 = find_obj(triangle.angle3)
        side1 = find_obj(triangle.side1)
        side2 = find_obj(triangle.side2)
        side3 = find_obj(triangle.side3)
        circumference = find_obj(triangle, 'circumference')
        area = find_obj(triangle, 'area')
        
        UNKNOWN = AttributeState.UNKNOWN
        KNOWN = AttributeState.KNOWN
        
        angles = [angle1, angle2, angle3]
        sides = [side1, side2, side3]
        angle_name = ['angle_A', 'angle_B', 'angle_C']
        line_name = ['line_BC', 'line_AC', 'line_AB']
        for permutation in [[0, 1, 2], [0, 2, 1], [1, 0, 2], \
                [1, 2, 0], [2, 0, 1], [2, 1, 0]]:
            pattern = TrianglePattern(init_value=UNKNOWN)
            value_pattern = TrianglePattern(init_value=UNKNOWN)
            
            def set_pattern(obj, attr_name):
                is_known = UNKNOWN if obj.attr_value is None else KNOWN
                pattern.__setattr__(attr_name, is_known)
                value_pattern.__setattr__(attr_name, obj)
                
            for i in range(3):
                angle = angles[permutation[i]]
                side = sides[permutation[i]]
                set_pattern(angle, angle_name[i])
                set_pattern(side, line_name[i])
            set_pattern(circumference, 'circumference')
            set_pattern(area, 'area')
            
            ret.append((pattern, value_pattern))

        return ret
                    
    def _extract_line_pattern(self, line: Line):
        return []
    
    def _extract_angle_pattern(self, angle: Angle):
        return []

