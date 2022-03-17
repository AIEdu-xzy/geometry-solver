from geometry_solver.relationship import ValueEquivalence


def index_equivalent_value(indexer, obj1, attr1, obj2, attr2):
        """Given two object's attributes, if they are equivalent,
        return valueEquivalent object, 
        else return None.
        """
        eq_conds = indexer.index_by_type(ValueEquivalence)
        for cond in eq_conds:
            r = cond.relationship
            obj_list = r.obj_list
            attr_list = r.attr_list
            if obj1 in obj_list and obj2 in obj_list \
                    and attr1 in attr_list and attr2 in attr_list:
                return cond
        return None
