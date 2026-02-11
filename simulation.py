import numpy as np
from config import (
    SPACE_MIN, SPACE_MAX,
    N_PARTICLE_TYPES, COLOR_DISTRIBUTION,
    FRICTION, DELTA_T, MAX_RADIUS
)
from interaction import Interaction
from scipy.spatial import cKDTree
from numba import njit
# --- Build particle types from setting ---
@njit
def apply_physics_jit(velocities, dv, effect_scale, delta_t, friction):
    velocities += (dv * effect_scale) * delta_t
    velocities *= friction
    return velocities

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
    return np.random.normal(0.0, 0.3, size=(n_particles, 2)).astype(float)

def init_color_distribution(types: np.ndarray) -> np.ndarray:
    """Initialize colors based on particle types."""
    return np.c_[COLOR_DISTRIBUTION[types], np.ones(len(types))]


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

        # interactions
        self.interaction = Interaction()
        self.max_distance = float(MAX_RADIUS) #from config
        self.effect_scale = 1.0

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

    def _wrap_positions(self):
        span = (SPACE_MAX - SPACE_MIN)
        self.positions = (self.positions - SPACE_MIN) % span + SPACE_MIN
        
    def step(self):
        dv = np.zeros_like(self.velocities)
        
        tree = cKDTree(self.positions)
        pairs = tree.query_pairs(self.max_distance)

        for i, j in pairs:
            dv[i] += self.interaction.interaction_effect(
                self.positions[i], self.positions[j],
                int(self.types[i]), int(self.types[j]),
                self.max_distance
            )
            dv[j] += self.interaction.interaction_effect(
                self.positions[j], self.positions[i],
                int(self.types[j]), int(self.types[i]),
                self.max_distance
            )

        self.velocities += np.random.uniform(-0.01, 0.01, size=self.velocities.shape)

        self.velocities = apply_physics_jit(
            self.velocities, dv, self.effect_scale, 
            float(DELTA_T), float(FRICTION)
        )
        
        self.positions += self.velocities * float(DELTA_T)
        
        self._wrap_positions()
        self.update_particles_view()

if __name__ == "__main__":
    sim = Simulation(
        [{"n": 103, "type": 2}, {"n": 14, "type": 0}]
    )
    print("n_particles:", sim.n_particles)
    print("particles shape:", sim.particles.shape)
    print(sim.particles[:5])
