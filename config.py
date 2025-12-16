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

# colors for each particle type (RGBA)
COLOR_DISTRIBUTION = np.array([
    [1.0, 0.0, 0.0],  # Red
    [0.0, 1.0, 0.0],  # Green
    [0.0, 0.0, 1.0],  # Blue
    [1.0, 1.0, 0.0],  # Yellow
])

friction = 0.99
delta_t = 0.5
MAX_RADIUS = 100, 100