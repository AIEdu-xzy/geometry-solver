from typing import List

from geometry_solver.relationship.relationship import Relationship
from geometry_solver.entity import Entity


class TwoSum(Relationship):

    def __init__(self, id_: 
            str, entity1: Entity, 
            attr1: str, 
            entity2: Entity, 
            attr2: str, 
            sum_value: float):
        super(TwoSum, self).__init__(id_)
        self.entity1 = entity1
        self.attr1 = attr1
        self.entity2 = entity2
        self.attr2 = attr2
        self.sum_value = sum_value

    def __str__(self):
        return 'TwoSum({})'.format(
            str(self.entity1) + '.' + self.attr1 + ' + ' \
            + str(self.entity2) + '.' + self.attr2) + ' = ' \
            + str(self.sum_value)

