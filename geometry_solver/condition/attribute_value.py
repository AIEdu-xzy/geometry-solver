from geometry_solver.condition.condition import Condition
from geometry_solver.entity import Entity
from geometry_solver.relationship import Relationship
from geometry_solver.target.target import Target
from geometry_solver.config import ROUND_PRECISION


class AttributeValue(Condition):
    """This class is responsible for storing value of konwn attribute.
    
    Usage
    ::
        >>> condition = AttributeEq(line_AB, length=1)
    """
    
    def __init__(self, obj, **attr_dict):
        super().__init__()
        self.obj = obj
        if len(attr_dict) != 1:
            raise ValueError("AttributeValue condition can only keep 1 attribute's value.")
        self.attr_name = list(attr_dict.keys())[0]
        self._attr_value = list(attr_dict.values())[0]

    def match(self, target: Target) -> bool:
        return self.obj == target.obj \
                and target.attr == self.attr_name
                
    @property
    def attr_value(self):
        return self._attr_value
    
    @attr_value.setter
    def attr_value(self, value):
        self._attr_value = value

    def __str__(self):
        value = round(self._attr_value, ROUND_PRECISION)
        return '{}.{}={}'.format(self.obj.id, self.attr_name, value)
    
    __repr__ = __str__

    def __keys(self):
        return (self.obj, self.attr_name, self._attr_value)

    def __hash__(self):
        return self.__keys().__hash__()

    def __eq__(self, other):
        if not isinstance(other, AttributeValue):
            return False
        return self.__keys() == other.__keys()
    
