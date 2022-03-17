

def attr_value_known_num(conditions):
    return sum([c.attr_value is not None for c in conditions])
    
