from typing import Union

from geometry_solver.indexer.base_indexer import BaseIndexer
from geometry_solver.entity.entity import Entity
from geometry_solver.condition.condition import Condition
from geometry_solver.graph.deduction_graph import DeductionGraph


class OwnershipIndexer(BaseIndexer):
    
    def __init__(self, 
            entity: Entity, 
            graph: DeductionGraph):
        # Key of the table is child entity, value of the table is a table
        # whose key is owner's type and value is owner object.
        self.table = {}
        self.build_index(entity, graph)
    
    def build_index(self, 
            entity: Entity, 
            graph: DeductionGraph):
        # Example of table:
        # {
        #     point_a: {
        #         Triangle: [triangle_abc, triangle_bcd]
        #     }
        # }
        for e in entity.children:
            for ch in e.children:
                if ch not in self.table:
                    self.table[ch] = {}
                if type(e) not in self.table[ch]:
                    self.table[ch][type(e)] = []
                self.table[ch][type(e)].append(e)
    
    def update_index(self, new_obj: Union[Condition, Entity]):
        if isinstance(new_obj, Entity):
            return NotImplemented
    
    def index(self, obj, owner_type):
        if obj not in self.table or owner_type not in self.table[obj]:
            return []
        return self.table[obj][owner_type]

