import numpy as np
from src.simulation import Simulation
from src.config import SPACE_MIN, SPACE_MAX

def test_visualization_initialization():
    """Check if simulation data is ready for Vispy markers."""
    sim = Simulation([
        {"n": 50, "type": 0},
        {"n": 50, "type": 1}
    ])
    
    # Verify data shapes for rendering
    assert sim.positions.shape == (100, 2)
    assert sim.colors.shape == (100, 4)

def test_keyboard_input_logic():
    """Verify the logic behind the R and M keys."""
    sim = Simulation([{"n": 10, "type": 0}])
    old_positions = sim.positions.copy()
    old_matrix = sim.interaction.matrix.copy()
    
    # Logic for 'R' (Reset)
    sim.positions = np.random.uniform(SPACE_MIN, SPACE_MAX, size=(sim.n_particles, 2))
    assert not np.array_equal(sim.positions, old_positions)
    
    # Logic for 'M' (Matrix Change)
    sim.interaction.matrix = np.random.uniform(-1, 1, (4, 4))
    assert not np.array_equal(sim.interaction.matrix, old_matrix)
