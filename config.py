import numpy as np

"""
These constants are used for initializing particle properties
and for visualization.
"""

# simulation space limits (has to be symmetric around zero)
SPACE_MIN = -10.0
SPACE_MAX = 10.0

# number of particle types
N_PARTICLE_TYPES = 4


# colors for each particle type (RGB)
COLOR_DISTRIBUTION = np.array([
    [0.70, 0.30, 1.00],  # Violett
    [0.75, 1.00, 0.80],  # Mint
    [1.00, 0.40, 0.70],  # Pink
    [0.10, 0.40, 1.00],  # Tiefblau
])

# simulation timing
FRICTION = 0.995
DELTA_T = 0.8
MAX_RADIUS = 6.0