from typing import List

from geometry_solver.condition import Condition
from geometry_solver.indexer.indexer import Indexer


class Theorem(object):
    
    name = 'base theorem'
    
    def __init__(self):
        pass
    
    def index(self, indexer: Indexer):
        """Find all sources and target conditions using indexer.

        :return: a list of [sources, target].
        """
        raise NotImplementedError
    
    def deduct(self, sources: List[Condition], target: Condition):
        """This method is used to perform a deduction.

        :param sources: a list of source condition.
        :param target: target condition.
        :return: deducted target condition.
        """
        raise NotImplementedError

