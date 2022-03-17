import numpy as np

from geometry_solver.policy.base_policy import BasePolicy


class BFSPolicy(BasePolicy):

    def __init__(self):
        super().__init__()

    def chose_theorem(self, problem, max_step=4):
        final_node = None
        q = queue.Queue()
        q.put(problem)
        next_step_num = 1
        current_step = 0
        step = 0
        while not q.empty() and current_step <= max_step:
            acc_num = 0
            for _ in tqdm(range(next_step_num), desc='Step {}'.format(current_step)):
                step += 1
                node = q.get()
                if node.solved:
                    final_node = node
                    break
                for node_copy in self._next_step_nodes(node):
                    acc_num += 1
                    q.put(node_copy)
            else:
                next_step_num = acc_num
                current_step += 1
                continue
            break

        print('Use step: {}'.format(current_step))
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

