import numpy as np

from src.config import SPACE_MIN, SPACE_MAX, MAX_RADIUS
from src.simulation import Simulation
from src.interaction import Interaction

# run with: python -m pytest -q test.py
def test_positions_update():
    sim = Simulation(setting=[{"n": 10, "type": 0}, {"n": 10, "type": 1}])
    p0 = sim.positions.copy()
    sim.step()
    assert not np.allclose(p0, sim.positions)


def test_attraction_repulsion_direction():
    inter = Interaction(matrix=np.array([
        [ 1.0, -1.0, 0.0, 0.0],
        [-1.0,  1.0, 0.0, 0.0],
        [ 0.0,  0.0, 0.0, 0.0],
        [ 0.0,  0.0, 0.0, 0.0],
    ], dtype=float))

    pos_i = np.array([0.0, 0.0])
    dist = 0.3 * MAX_RADIUS
    pos_j = np.array([dist, 0.0])

    eff_attract = inter.interaction_effect(pos_i, pos_j, 0, 0, MAX_RADIUS)
    eff_repulse = inter.interaction_effect(pos_i, pos_j, 0, 1, MAX_RADIUS)

    direction = (pos_j - pos_i) / np.linalg.norm(pos_j - pos_i)

    assert np.linalg.norm(eff_attract) > 0
    assert np.linalg.norm(eff_repulse) > 0
    assert np.dot(eff_attract, direction) > 0
    assert np.dot(eff_repulse, direction) < 0


def test_simulation_stability():
    sim = Simulation(setting=[{"n": 15, "type": 0}, {"n": 15, "type": 1}])
    for _ in range(50):
        sim.step()

    assert np.isfinite(sim.positions).all()
    assert (sim.positions[:, 0] >= SPACE_MIN).all()
    assert (sim.positions[:, 0] <= SPACE_MAX).all()
    assert (sim.positions[:, 1] >= SPACE_MIN).all()
    assert (sim.positions[:, 1] <= SPACE_MAX).all()

