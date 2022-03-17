from typing import List, Union

from geometry_solver.relationship.relationship import Relationship
from geometry_solver.entity import Entity


class ValueProportion(Relationship):
    """Model proportion relationship between mutiplt attributes.
    
    For example:
        if AB = 2 * CD, then object
        ValueProportion(id='AB = 2 * CD', 
            obj_list=[line_ab, line_cd],
            attr_list=['length', 'length'],
            weight=[1, 2])
        is created.
    """
    
    def __init__(
            self, 
            id_: str, 
            obj_list: List[Union[Entity, Relationship]],
            attr_list: List[str], 
            weight:List[float]):
        super().__init__(id_)
        self.obj_list = obj_list
        self.attr_list = attr_list
        self.weight = weight
    
    def __str__(self):
        members = []
        for i in range(len(self.obj_list)):
            members.append('{} {}.{}'.format(
                '' if self.weight[i] == 1 else self.weight[i],
                self.obj_list[i], 
                self.attr_list[i]))
        return ' = '.join(members)

