import pytest
import numpy as np
from src.config import SPACE_MIN, SPACE_MAX, MAX_RADIUS
from src.simulation import Simulation, calculate_forces_jit

def test_simulation_default_init():
    """Tests if simulation initializes with default settings when None is provided."""
    sim = Simulation(setting=None)
    # Default is 100 particles per type (4 types), so 400 total
    assert sim.n_particles == 400
    assert hasattr(sim, 'interaction')

def test_simulation_update_view_sync():
    """Checks if update_particles_view correctly syncs internal state."""
    sim = Simulation(setting=[{"n": 1, "type": 0}])
    new_pos = np.array([[0.5, 0.5]])
    sim.positions = new_pos
    sim.update_particles_view()
    # Check if the packed 'particles' array was updated
    assert np.array_equal(sim.particles[0, 0:2], new_pos[0])

def test_simulation_type_range_error():
    """Tests if types_from_setting raises ValueError for out-of-range types."""
    from src.simulation import types_from_setting
    # Type 10 is out of range if N_PARTICLE_TYPES is 4
    with pytest.raises(ValueError, match="out of range"):
        types_from_setting([{"n": 1, "type": 10}])

def test_simulation_bounciness_logic():
    """Tests the position_bounciness logic for wall collisions."""
    sim = Simulation(setting=[{"n": 1, "type": 0}], bounciness=0.5)
    # Place particle exactly at the boundary to trigger bounce
    sim.positions[0] = np.array([SPACE_MIN - 0.1, 0.5])
    sim.velocities[0] = np.array([-1.0, 0.0])
    
    sim.position_bounciness()
    
    # Position should be mirrored back and velocity reflected
    assert sim.positions[0, 0] > SPACE_MIN
    assert sim.velocities[0, 0] > 0 # Should now move in positive direction