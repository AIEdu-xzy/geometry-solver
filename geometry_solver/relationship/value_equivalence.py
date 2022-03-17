from typing import List, Union

from geometry_solver.relationship.relationship import Relationship
from geometry_solver.relationship.value_proportion import ValueProportion
from geometry_solver.entity import Entity


class ValueEquivalence(ValueProportion):
    """Model equicalence relationship between mutiplt attributes.
    
    For example:
        if AB = CD, then object
        ValueEquivalence(id='AB_CD', 
            obj_list=[line_ab, line_cd],
            attr_list=['length', 'length'])
        is created.
    """
    
    def __init__(
            self, 
            id_: str, 
            obj_list: List[Union[Entity, Relationship]],
            attr_list: List[str]):
        super().__init__(id_, obj_list, attr_list, [1]*len(obj_list))

