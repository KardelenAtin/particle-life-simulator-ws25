import numpy as np
from config import SPACE_MIN, SPACE_MAX

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

class Simulation:
    def __init__(self):
        self.interaction_matrix = [
            [0, 1, -1, 0],
            [-1, 0, 1, 0],
            [1, -1, 0, 0],
            [0, 0, 0, 0]
        ]