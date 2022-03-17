import numpy as np

from geometry_solver.policy.base_policy import BasePolicy


class BeamSearchPolicy(BasePolicy):

    def __init__(self):
        super().__init__()

    def chose_theorem(self, problem,  beam=20, max_step=None):
        final_node = None
        beam_nodes = [problem]
        step = 0
        while max_step is None or step < max_step:
            # Check termination.
            for node in beam_nodes:
                if node.solved:
                    final_node = node
                    break
            else:
                # Search next step.
                step += 1
                next_nodes = []
                for node in tqdm(beam_nodes,  desc='Step {}'.format(step)):
                    next_nodes += self._next_step_nodes(node)
                np.random.shuffle(next_nodes)
                beam_nodes = next_nodes[:beam]
                continue
            break
        return final_node
    
    def _next_step_nodes(self, node):
        nodes = []
        actions = node.valid_actions
        for action in actions:
            node_copy = copy.deepcopy(node)
            success = node_copy.take_action(action)
            if success:
                nodes.append(node_copy)
        return nodes

