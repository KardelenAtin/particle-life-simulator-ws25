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
    [1.0, 0.0, 0.0],  # Red
    [0.0, 1.0, 0.0],  # Green
    [0.0, 0.0, 1.0],  # Blue
    [1.0, 1.0, 0.0],  # Yellow
])

# simulation timing
FRICTION = 0.995
DELTA_T = 0.8
MAX_RADIUS = 6.0