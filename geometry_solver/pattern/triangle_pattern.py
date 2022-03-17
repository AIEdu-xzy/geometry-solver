from geometry_solver.pattern.attribute_state import AttributeState
from geometry_solver.pattern.pattern import Pattern


class TrianglePattern(Pattern):
    __slots__ = [
        'angle_A',
        'angle_B',
        'angle_C',
        'line_BC',
        'line_AC',
        'line_AB',
        'circumference',
        'area'
    ]

    def __init__(self,
            angle_A=AttributeState.NOT_MATTER,
            angle_B=AttributeState.NOT_MATTER,
            angle_C=AttributeState.NOT_MATTER,
            line_BC=AttributeState.NOT_MATTER,
            line_AC=AttributeState.NOT_MATTER,
            line_AB=AttributeState.NOT_MATTER,
            circumference=AttributeState.NOT_MATTER,
            area=AttributeState.NOT_MATTER,
            init_value=None):
        if init_value is not None:
            self.angle_A = init_value
            self.angle_B = init_value
            self.angle_C = init_value
            self.line_BC = init_value
            self.line_AC = init_value
            self.line_AB = init_value
            self.circumference = init_value
            self.area = init_value
        else:
            self.angle_A = angle_A
            self.angle_B = angle_B
            self.angle_C = angle_C
            self.line_BC = line_BC
            self.line_AC = line_AC
            self.line_AB = line_AB
            self.circumference = circumference
            self.area = area

    def __eq__(self, other):
        """Determin two pattern is the same."""
        if not isinstance(other, TrianglePattern):
            return False
            
        NOT_MATTER = AttributeState.NOT_MATTER
        
        def match(attr1, attr2):
            if attr1 == NOT_MATTER or attr2 == NOT_MATTER:
                return True
            return attr1 == attr2
        
        return match(self.angle_A, other.angle_A) \
                and match(self.angle_B, other.angle_B) \
                and match(self.angle_C, other.angle_C) \
                and match(self.line_AB, other.line_AB) \
                and match(self.line_BC, other.line_BC) \
                and match(self.line_AC, other.line_AC) \
                and match(self.circumference, other.circumference) \
                and match(self.area, other.area)

    def __str__(self):
        
        def translate(value):
            if value == AttributeState.KNOWN:
                return 'KNOWN'
            elif value == AttributeState.UNKNOWN:
                return 'UNKNOWN'
            elif value == AttributeState.NOT_MATTER:
                return 'NOT MATTER'
            elif value == None:
                return 'None'
            else:
                return str(value)

        return '(TrianglePattern:' \
              + ' angle_A: ' + translate(self.angle_A) \
              + ' angle_B: ' + translate(self.angle_B) \
              + ' angle_C: ' + translate(self.angle_C) \
              + ' line_BC: ' + translate(self.line_BC) \
              + ' line_AC: ' + translate(self.line_AC) \
              + ' line_AB: ' + translate(self.line_AB) \
              + ' circumference: ' + translate(self.circumference) \
              + ' area: ' + translate(self.area) \
              + ')'
        
    __repr__ = __str__

