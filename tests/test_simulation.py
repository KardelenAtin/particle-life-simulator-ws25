import pytest
import numpy as np
from src.config import SPACE_MIN, SPACE_MAX, MAX_RADIUS
from src.simulation import Simulation, calculate_forces_jit

def test_positions_update():
    """Checks if particles move after a simulation step."""
    sim = Simulation(setting=[{"n": 10, "type": 0}])
    p0 = sim.positions.copy()
    sim.step()
    assert not np.allclose(p0, sim.positions)

def test_jit_force_logic():
    """
    Checks if JIT forces correctly attract.
    Distance is set to 10.0 to ensure particles are in the attraction zone.
    """
     # Two particles, same type, should attract each other
    pos = np.array([[0.0, 0.0], [10.0, 0.0]], dtype=float)
    types = np.array([0, 0], dtype=int)
    matrix = np.zeros((4, 4))
    matrix[0, 0] = 1.0  # Attraction for same type
    
    dv = calculate_forces_jit(pos, types, matrix, float(MAX_RADIUS))
    
    # Particle 0 should be pulled towards Particle 1 (positive x-direction)
    assert dv[0, 0] > 0 

def test_wrap_boundary():
    """Checks if particles reappear on the opposite side (periodic boundaries)."""
    sim = Simulation([{"n": 1, "type": 0}])
    # Force particle outside left wall
    sim.positions[0] = np.array([SPACE_MAX + 5.0, 0.0])
    
    sim._wrap_positions()
    
    # Must be inside now and velocity reflected
    assert sim.positions[0, 0] >= SPACE_MIN
    assert sim.positions[0, 0] <= SPACE_MAX

def test_simulation_invalid_inputs():
    """Tests error handling for invalid inputs to increase coverage."""
    # test invalid setting type
    with pytest.raises(ValueError, match="mass must be greater than zero"):
        Simulation(setting=[{"n": 10, "type": 0}], mass=-1.0)
    
    # test invalid bounciness
    with pytest.raises(ValueError, match="bounciness must be between 0 and 1"):
        Simulation(setting=[{"n": 10, "type": 0}], bounciness=1.5)