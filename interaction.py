# for interaction interaction matrix
import numpy as np
from simulation import init_color_distribution, init_positions, init_types

class Simulation:
    def __init__(self):
        n_particles = 4
        self.positions = init_positions(n_particles)
        self.types = init_types(n_particles)
        self.colors = init_color_distribution(self.types)
        self.interaction_matrix = np.array([
            [0, 1, -1, 0],
            [-1, 0, 1, 0],
            [1, -1, 0, 0],
            [0, 0, 0, 0]
        ])

    def step(self):
        for i in range (len(self.positions)):
            for j in range (len(self.positions)):
                if i == j:
                    continue

                ti = self.types[i]
                tj = self.types[j]

                strength = self.interaction_matrix[ti][tj]