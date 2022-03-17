from typing import List


class Entity(object):
    
    def __init__(self, id_):
        self.id = id_
        self.children = set()
    
    def _add_entity(self, entity):
        # Add children recursively.
        for e in entity.children:
            self._add_entity(e)
        self.children.add(entity)
    
    def add_entity(self, *entities):
        for entity in entities:
            self._add_entity(entity)

    def find_child(self, id_, type_=None):
        for entity in self.children:
            if entity.id == id_:
                if type_ is None:
                    return entity
                elif type(entity) == type_:
                    return entity
        return None

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return type(self) == type(other) \
               and self.id == other.id
    
    def __str__(self):
        return '(' \
            + 'Entity: ' \
            + self.id \
            + ', has ' \
            + str(len(self.children)) \
            + ' children)'

