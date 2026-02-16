import numpy as np

class Interaction:
    def __init__(self, matrix: np.ndarray | None = None):
        if matrix is None:
            matrix = np.array([
                [ 0.2, 0.5, -0.4,  0.0],  
                [-0.2,  0.2,  0.5, -0.4],  
                [-0.4,  -0.2,  0.2, 0.5],  
                [ 0.5, -0.4, -0.2,  0.2],  
            ], dtype=float)
        self.matrix = matrix.astype(float)

    def get_strength(self, type_i: int, type_j: int) -> float:
        return float(self.matrix[type_i, type_j])

    def interaction_effect(
        self,
        pos_i: np.ndarray,
        pos_j: np.ndarray,
        type_i: int,
        type_j: int,
        max_distance: float,
    ) -> np.ndarray:
        strength = self.get_strength(type_i, type_j)
        if strength == 0:
            return np.zeros(2, dtype=float)

        delta = pos_j - pos_i
        dist = float(np.linalg.norm(delta))
        if dist == 0.0 or dist > max_distance:
            return np.zeros(2, dtype=float)

        direction = delta / dist
        r = dist / max_distance  # 0..1

        def smoothstep(x: float) -> float:
            x = float(np.clip(x, 0.0, 1.0))
            return x * x * (3 - 2 * x)

        repulsion_radius = 0.15
        attraction_radius = 0.60

        if r < repulsion_radius:
            t = r / repulsion_radius
            factor = -(1.0 - smoothstep(t))   
        elif r < attraction_radius:
            t = (r - repulsion_radius) / (attraction_radius - repulsion_radius)
            factor = smoothstep(1.0 - t)     
        else:
            factor = 0.0

        return direction * strength * factor




