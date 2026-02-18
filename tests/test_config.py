import numpy as np
from src.config import SPACE_MIN, SPACE_MAX, N_PARTICLE_TYPES, COLOR_DISTRIBUTION


def test_config_logic():
    """Basic sanity checks for simulation constants."""
    #Check space boundaries 
    assert SPACE_MAX > SPACE_MIN 
    assert SPACE_MAX == -SPACE_MIN

    #Check particle types and colors 
    assert N_PARTICLE_TYPES == len(COLOR_DISTRIBUTION)
    assert COLOR_DISTRIBUTION.shape == (4,3)

    #Check color values range [0,1]
    assert np.all((COLOR_DISTRIBUTION >= 0) & (COLOR_DISTRIBUTION <= 1))