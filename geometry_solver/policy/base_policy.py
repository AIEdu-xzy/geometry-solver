from geometry_solver.theorem import valid_theorem


class BasePolicy(object):

    def __init__(self):
        self.theorems = [th() for th in valid_theorem]

    def chose_theorem(self, problem):
        pass

