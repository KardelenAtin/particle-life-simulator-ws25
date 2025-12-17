import numpy as np

from config import SPACE_MIN, SPACE_MAX, MAX_RADIUS
from simulation import Simulation
from interaction import Interaction


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
    pos_j = np.array([1.0, 0.0])

    assert inter.interaction_effect(pos_i, pos_j, 0, 0, MAX_RADIUS)[0] > 0
    assert inter.interaction_effect(pos_i, pos_j, 0, 1, MAX_RADIUS)[0] < 0


def test_simulation_stability():
    sim = Simulation(setting=[{"n": 15, "type": 0}, {"n": 15, "type": 1}])
    for _ in range(50):
        sim.step()

    assert np.isfinite(sim.positions).all()
    assert (sim.positions[:, 0] >= SPACE_MIN).all()
    assert (sim.positions[:, 0] <= SPACE_MAX).all()
    assert (sim.positions[:, 1] >= SPACE_MIN).all()
    assert (sim.positions[:, 1] <= SPACE_MAX).all()

