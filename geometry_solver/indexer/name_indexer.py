from typing import Union

from geometry_solver.indexer.base_indexer import BaseIndexer
from geometry_solver.entity.entity import Entity
from geometry_solver.condition.condition import Condition
from geometry_solver.graph.deduction_graph import DeductionGraph


class NameIndexer(BaseIndexer):
    
    def __init__(self,
            entity: Entity, 
            graph: DeductionGraph):
        self.table = {}
        self.build_index(entity, graph)
    
    def build_index(self,
            entity: Entity, 
            graph: DeductionGraph):
        for e in entity.children:
            self.update_index(e)
    
    def update_index(self, new_obj: Union[Condition, Entity]):
        if isinstance(new_obj, Entity):
            if new_obj.id not in self.table:
                self.table[new_obj.id] = []
            self.table[new_obj.id].append(new_obj)
    
    def index(self, name):
        if name not in self.table:
            return []
        return self.table[name]