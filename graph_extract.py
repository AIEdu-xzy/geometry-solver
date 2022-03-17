import networkx as nx


def create_graph_for_problems(problems):
    return [create_graph_for_problem(p) for p in problems]
    

def create_graph_for_problem(problem):
    G = nx.DiGraph()
    entity_list = problem.entity.children
    relationships = [cond.relationship for cond in problem.conditions \
            if type(cond) == RelationshipBased]
    
    for e in entity_list:
        
    
    for r in relationships:
    
    
