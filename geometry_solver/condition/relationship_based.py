from geometry_solver.relationship import Relationship
from geometry_solver.condition.condition import Condition
from geometry_solver.target.target import Target


class RelationshipBased(Condition):
    """RelationshipBased is the wrapper of a relationship.
    
    Usage
    ::
        >>> condition = RelationshipBased(parallel_AB_CD)

    """
    
    def __init__(self, relationship: Relationship):
        super().__init__()
        self.relationship = relationship
    
    def match(self, target: Target) -> bool:
        return False
    
    def __hash__(self):
        return (self.relationship).__hash__()

    def __str__(self):
        return str(self.relationship)
    
    def __repr__(self):
        return str(self.relationship)

