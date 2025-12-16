import random
import numpy as np
from config import SPACE_MIN, SPACE_MAX, N_PARTICLE_TYPES, COLOR_DISTRIBUTION , friction, delta_t, MAX_RADIUS

# --- Particle Initialization Functions ---

def init_positions(n_particles: int) -> np.ndarray:
    """Generate initial particle positions within simulation bounds."""
    return np.random.uniform(SPACE_MIN, SPACE_MAX, size=(n_particles, 2)).astype(float)


def init_types(n_particles: int) -> np.ndarray:
    """Assign random particle type to each particle."""
    return np.random.randint(0, N_PARTICLE_TYPES, size=n_particles, dtype=int)


def init_color_distribution(types: np.ndarray) -> np.ndarray:
    """Initialize colors based on particle types."""
    return COLOR_DISTRIBUTION[types]


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

# --- Simulation Class ---
class Simulation:
    def __init__(self, setting = [{"n":3,"type":2},{"n":4,"type":0}]): 
        particles = []
        for s in setting:
            for p in range(s["n"]):
                particle = np.array([random.randint(0, 100), random.randint(0, 100), 0, 0, s["type"]])
                particles.append(particle)
        self.particles = np.vstack(particles)
        print(self.particles)

        
if __name__ == "__main__":
    ll= Simulation([{"n":103,"type":2},{"n":14,"type":0}])