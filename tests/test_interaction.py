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

def test_interaction_effect_zero_strength():
    """If strength is 0, effect must be a zero vector."""
    matrix = np.zeros((4, 4))
    inter = Interaction(matrix=matrix)
    pos_i = np.array([0.0, 0.0])
    pos_j = np.array([1.0, 0.0])
    
    effect = inter.interaction_effect(pos_i, pos_j, 0, 0, 10.0)
    assert np.array_equal(effect, np.array([0.0, 0.0]))

def test_interaction_effect_distance_logic():
    """Checks repulsion and attraction zones."""
    inter = Interaction() # Default matrix
    max_d = 10.0
    pos_i = np.array([0.0, 0.0])
    
    # 1. Too far away (> max_distance)
    pos_far = np.array([11.0, 0.0])
    effect_far = inter.interaction_effect(pos_i, pos_far, 0, 0, max_d)
    assert np.all(effect_far == 0)

    # 2. Repulsion zone (r < 0.15)
    # Strength for (0,0) is 0.2 (positive). Repulsion factor is negative.
    # Total effect should be negative (pushing away)
    pos_close = np.array([0.1, 0.0]) 
    effect_close = inter.interaction_effect(pos_i, pos_close, 0, 0, max_d)
    assert effect_close[0] < 0 

    # 3. Attraction zone (0.15 < r < 0.60)
    # Strength for (0,0) is 0.2. Attraction factor is positive.
    # Total effect should be positive (pulling towards)
    pos_mid = np.array([3.0, 0.0]) # r = 0.3
    effect_mid = inter.interaction_effect(pos_i, pos_mid, 0, 0, max_d)
    assert effect_mid[0] > 0