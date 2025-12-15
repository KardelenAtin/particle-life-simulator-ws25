import numpy as np

class Simulation:
    def __init__(self):
        self.interaction_matrix = [
            [0, 1, -1, 0],
            [-1, 0, 1, 0],
            [1, -1, 0, 0],
            [0, 0, 0, 0]
        ]