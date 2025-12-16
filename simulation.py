import random
import numpy as np
from config import SPACE_MIN, SPACE_MAX, N_PARTICLE_TYPES, COLOR_DISTRIBUTION 


def init_masses(n_particles: int, mass: float = 1.0) -> np.ndarray:
    """
    Assign a physical mass to each particle.
    """
    if mass <= 0:
        raise ValueError("mass must be greater than zero")

    return np.full(n_particles, mass) 

def init_bounciness(n_particles: int, bounciness: float = 0.9) -> np.ndarray:
    """
    Assign a bounciness coefficient to each particle.
    """
    if not 0.0 <= bounciness <= 1.0:
        raise ValueError("bounciness must be between 0 and 1")

    return np.full(n_particles, bounciness)

def init_velocities(n_particles: int) -> np.ndarray:
    """
    Initialize particle velocities.
    Minimal version: all start with 0 velocity.
    Returns shape: (n_particles, 2)
    """
    return np.zeros((n_particles, 2), dtype=float)

def init_particles(n_particles: int):
    """
    Convenience function: returns all particle arrays.
    """
    positions = init_positions(n_particles)
    types = init_types(n_particles)
    colors = init_color_distribution(types)
    velocities = init_velocities(n_particles)
    masses = init_masses(n_particles)
    bounciness = init_bounciness(n_particles)

    return positions, velocities, types, colors, masses, bounciness


class Simulation:
    def __init__(
            self,
            settig = None,
            mass: float = 1.0,
            bounciness: float = 1.0      
        ):

        if setting is None:
            setting = [{"n":3,"type":2},{"n":4, "type":0}]

        self.types = np.column_stack([
            self.positions[:,0],
            self.positions[:,1],
            self.velocities[:,0],
            self.velocities[:,1],
            self.types
        ]).astype(float)

    def update_particles_view(self):
        self.particles[:, 0:2] = self.positions
        self.particles[:, 2:4] = self.velocities
        self.particles[:, 4] = self.types

if __name__ == "__main__":
    sim = Simulation([{"n": 103, "typ": 2}, {"n": 14, "typ": 0}])
    print("n_particles:", sim.n_particles)
    print("particles shape:", sim.particles.shape)
    print(sim.particles[:5])


