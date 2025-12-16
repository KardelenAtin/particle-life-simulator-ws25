import numpy as np
from config import (
    SPACE_MIN, SPACE_MAX,
    N_PARTICLE_TYPES, COLOR_DISTRIBUTION,
    friction, delta_t, MAX_RADIUS
)

# --- Build particle types from setting ---

def types_from_setting(setting) -> np.ndarray:
    """
    setting = [{"n": 3, "type": 2}, {"n": 4, "type": 0}]
    """
    types = []
    for s in setting:
        n = int(s["n"])
        t = int(s["type"])
        if not (0 <= t < N_PARTICLE_TYPES):
            raise ValueError(
                f"Particle type {t} out of range [0, {N_PARTICLE_TYPES - 1}]"
            )
        types.extend([t] * n)
    return np.array(types, dtype=int)

# --- Particle Initialization Functions ---

def init_positions(n_particles: int) -> np.ndarray:
    """Generate initial particle positions within simulation bounds."""
    return np.random.uniform(
        SPACE_MIN, SPACE_MAX, size=(n_particles, 2)
    ).astype(float)


def init_velocities(n_particles: int) -> np.ndarray:
    """
    Initialize particle velocities.
    Minimal version: all start with 0 velocity.
    Returns shape: (n_particles, 2)
    """
    return np.zeros((n_particles, 2), dtype=float)


def init_color_distribution(types: np.ndarray) -> np.ndarray:
    """Initialize colors based on particle types."""
    return COLOR_DISTRIBUTION[types]


def init_masses(n_particles: int, mass: float = 1.0) -> np.ndarray:
    """
    Assign a physical mass to each particle.
    """
    if mass <= 0:
        raise ValueError("mass must be greater than zero")
    return np.full(n_particles, mass, dtype=float)


def init_bounciness(n_particles: int, bounciness: float = 0.9) -> np.ndarray:
    """
    Assign a bounciness coefficient to each particle.
    """
    if not 0.0 <= bounciness <= 1.0:
        raise ValueError("bounciness must be between 0 and 1")
    return np.full(n_particles, bounciness, dtype=float)


# --- Simulation Class ---

class Simulation:
    def __init__(
        self,
        setting=None,
        mass: float = 1.0,
        bounciness: float = 0.9
    ):
        if setting is None:
            setting = [{"n": 3, "type": 2}, {"n": 4, "type": 0}]

        # particle types and count
        self.types = types_from_setting(setting)
        self.n_particles = self.types.shape[0]

        # particle state
        self.positions = init_positions(self.n_particles)
        self.velocities = init_velocities(self.n_particles)
        self.colors = init_color_distribution(self.types)
        self.masses = init_masses(self.n_particles, mass=mass)
        self.bounciness = init_bounciness(self.n_particles, bounciness=bounciness)

        # packed view [x, y, vx, vy, type]
        self.particles = np.column_stack([
            self.positions[:, 0],
            self.positions[:, 1],
            self.velocities[:, 0],
            self.velocities[:, 1],
            self.types
        ]).astype(float)

    def update_particles_view(self):
        """Sync packed particle view with positions / velocities."""
        self.particles[:, 0:2] = self.positions
        self.particles[:, 2:4] = self.velocities
        self.particles[:, 4] = self.types


if __name__ == "__main__":
    sim = Simulation(
        [{"n": 103, "type": 2}, {"n": 14, "type": 0}]
    )
    print("n_particles:", sim.n_particles)
    print("particles shape:", sim.particles.shape)
    print(sim.particles[:5])
