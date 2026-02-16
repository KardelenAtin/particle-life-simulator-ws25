import numpy as np
from src.config import (
    SPACE_MIN, SPACE_MAX,
    N_PARTICLE_TYPES, COLOR_DISTRIBUTION,
    FRICTION, DELTA_T, MAX_RADIUS
)
from src.interaction import Interaction
from numba import njit

# --- HIGH-PERFORMANCE COMPUTATION LOGIC (Numba JIT) ---

@njit
def calculate_forces_jit(positions, types, matrix, max_dist):
    """
    Computes interaction forces using a double-loop.
    Optimized via Numba for high-performance particle physics.
    """
    n = positions.shape[0]
    dv = np.zeros_like(positions)
    
    # Radii for force zones (repulsion vs attraction)
    r_rep = 0.15 * max_dist 
    r_att = 0.60 * max_dist

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            dx = positions[j, 0] - positions[i, 0]
            dy = positions[j, 1] - positions[i, 1]
            dist = np.sqrt(dx*dx + dy*dy)

            if 0 < dist < max_dist:
                strength = matrix[int(types[i]), int(types[j])]
                r_norm = dist / max_dist
                
                # Force calculation (Smoothstep-like behavior)
                factor = 0.0
                if r_norm < 0.15: # Repulsion
                    t = r_norm / 0.15
                    factor = -(1.0 - (t * t * (3 - 2 * t)))
                elif r_norm < 0.60: # Attraction
                    t = (r_norm - 0.15) / (0.60 - 0.15)
                    factor = (1.0 - (t * t * (3 - 2 * t)))
                
                dv[i, 0] += (dx / dist) * strength * factor
                dv[i, 1] += (dy / dist) * strength * factor
                
    return dv

@njit
def apply_physics_jit(velocities, dv, effect_scale, delta_t, friction):
    """Updates velocities based on calculated forces and friction."""
    velocities += (dv * effect_scale) * delta_t
    velocities *= friction
    return velocities

# --- Particle Initialization Functions ---

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

def init_positions(n_particles: int) -> np.ndarray:
    """Generate initial particle positions within simulation."""
    return np.random.uniform(SPACE_MIN, SPACE_MAX, size=(n_particles, 2))

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
        """Initializes the simulation environment and particles."""
        if setting is None:
            setting = [{"n": 100, "type": i} for i in range(4)]

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
        self.max_distance = float(MAX_RADIUS)
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
        """Applies periodic boundary conditions (wrap-around)."""
        span = (SPACE_MAX - SPACE_MIN)
        self.positions = (self.positions - SPACE_MIN) % span + SPACE_MIN

    def position_bounciness(self):
        """Bounce off boundaries, scaling rebound velocity by bounciness."""
        for dim in (0, 1):
            low, high = SPACE_MIN, SPACE_MAX
            # lower wall
            mask_low = self.positions[:, dim] < low
            if np.any(mask_low):
                self.positions[mask_low, dim] = low + (low - self.positions[mask_low, dim])
                self.velocities[mask_low, dim] *= -self.bounciness[mask_low]
            # upper wall
            mask_high = self.positions[:, dim] > high
            if np.any(mask_high):
                self.positions[mask_high, dim] = high - (self.positions[mask_high, dim] - high)
                self.velocities[mask_high, dim] *= -self.bounciness[mask_high]

    def step(self):
        """Executes one simulation step."""
        # 1. JIT Force Calculation
        dv = calculate_forces_jit(
            self.positions, 
            self.types, 
            self.interaction.matrix, 
            self.max_distance
        )

        dv /= self.masses[:, None]

        # 2. Physics Update
        self.velocities += np.random.uniform(-0.01, 0.01, size=self.velocities.shape)
        self.velocities = apply_physics_jit(
            self.velocities, dv, self.effect_scale, 
            float(DELTA_T), float(FRICTION)
        )
        
        self.positions += self.velocities * float(DELTA_T)
        
        # 3. Boundary handling & view sync
        self.position_bounciness()
        self.update_particles_view()

if __name__ == "__main__":
    sim = Simulation([{"n": 100, "type": 0}])
    sim.step()
    print("n_particles:", sim.n_particles)           