import numpy as np
import pytest
from src.config import SPACE_MIN, SPACE_MAX, MAX_RADIUS
from src.simulation import Simulation, calculate_forces_jit

def test_positions_update():
    """Check if particles actually move after a step."""
    sim = Simulation(setting=[{"n": 10, "type": 0}])
    p0 = sim.positions.copy()
    sim.step()
    assert not np.allclose(p0, sim.positions)

def test_jit_force_logic():
    """ 
    Checks if JIT forces correctly attract/repulse.
    """
    # Two particles, same type
    pos = np.array([[0.0, 0.0], [2.0, 0.0]], dtype=float)
    types = np.array([0, 0], dtype=int)
    # Matrix with positive value at [0,0] -> Attraction
    matrix = np.zeros((4, 4))
    matrix[0, 0] = 1.0
    
    dv = calculate_forces_jit(pos, types, matrix, MAX_RADIUS)
    
    # Particle 0 should be pulled towards Particle 1 (positive x-direction)
    assert dv[0, 0] > 0 

def test_bounciness_boundary():
    """New test: Check if the bounce-back logic works."""
    sim = Simulation([{"n": 1, "type": 0}], bounciness=0.8)
    # Force particle outside left wall
    sim.positions[0] = np.array([SPACE_MIN - 1.0, 0.0])
    sim.velocities[0] = np.array([-5.0, 0.0])
    
    sim.position_bounciness()
    
    # Must be inside now and velocity reflected
    assert sim.positions[0, 0] > SPACE_MIN
    assert sim.velocities[0, 0] > 0

def test_simulation_stability():
    """stability test with a small update for velocities."""
    sim = Simulation(setting=[{"n": 10, "type": i} for i in range(4)])
    for _ in range(50):
        sim.step()

    assert np.isfinite(sim.positions).all()
    assert np.isfinite(sim.velocities).all()
    # Boundary checks
    assert (sim.positions >= SPACE_MIN).all()
    assert (sim.positions <= SPACE_MAX).all()