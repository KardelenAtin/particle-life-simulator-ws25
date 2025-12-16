import numpy as np
from config import SPACE_MIN, SPACE_MAX, N_PARTICLE_TYPES, COLOR_DISTRIBUTION

def init_positions(n_particles: int) -> np.ndarray:
    """
    Generate initial particle positions within simulation bounds.
    """
    positions = np.random.uniform(
        low=SPACE_MIN,
        high=SPACE_MAX,
        size=(n_particles, 2)
    )
    return positions

def init_types(n_particles: int) -> np.ndarray:
    """
    Assign random particle type to each particle.
    """
    types = np.random.randint(
        low=0,
        high=N_PARTICLE_TYPES,
        size=n_particles
    )
    return types

def init_color_distribution(types: np.ndarray) -> np.ndarray:
    """
    Initialize colors based on particle types
    """
    colors = COLOR_DISTRIBUTION[types]
    return colors

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

                strenth = self.interaction_matrix[ti][tj]