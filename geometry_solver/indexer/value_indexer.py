from typing import Union

from geometry_solver.indexer.base_indexer import BaseIndexer
from geometry_solver.condition.attribute_value import AttributeValue
from geometry_solver.condition.condition import Condition
from geometry_solver.graph.deduction_graph import DeductionGraph
from geometry_solver.entity.entity import Entity


class ValueIndexer(BaseIndexer):
    
    def __init__(self,
            entity: Entity, 
            graph: DeductionGraph):
        self.table = {}
        self.build_index(entity, graph)
    
    def build_index(self, 
            entity: Entity, 
            graph: DeductionGraph):
        for cond in graph.conditions:
            self.update_index(cond)
    
    def update_index(self, new_obj: Union[Condition, Entity]):
        if type(new_obj) == AttributeValue:
            value = new_obj.attr_value
            if value not in self.table:
                self.table[value] = []
            self.table[value].append(new_obj)
    
    def index(self, value):
        if value not in self.table:
            return []
        return self.table[value]