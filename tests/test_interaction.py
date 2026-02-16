import numpy as np
from src.interaction import Interaction

def test_interaction_default_matrix():
    """Checks if the default 4x4 matrix is initialized correctly."""
    inter = Interaction()
    assert inter.matrix.shape == (4, 4)
    # Check value from your code: type 0 to type 1 should be 0.5
    assert inter.get_strength(0, 1) == 0.5

def test_interaction_custom_matrix():
    """Checks if a custom matrix is correctly stored and accessed."""
    custom = np.ones((2, 2)) * 0.9
    inter = Interaction(matrix=custom)
    assert inter.get_strength(0, 1) == 0.9

