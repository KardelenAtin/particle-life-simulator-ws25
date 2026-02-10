import numpy as np

class Interaction:

    def __init__(self, matrix: np.ndarray | None = None):
        if matrix is None:
            matrix = np.array([
                [ 0.1,  1.0, -1.0,  0.5], # Rot interagiert mit Gelb
                [-1.0,  0.1,  1.0, -0.5], 
                [ 1.0, -1.0,  0.1,  0.2], 
                [ 0.4, -0.2,  0.3,  0.1], 
            ], dtype=float)
        self.matrix = matrix.astype(float)

    def get_strength(self, type_i: int, type_j: int) -> float:
        """
        Return the interaction strength between two particle types
        """
        return float(self.matrix[type_i, type_j])

    def interaction_effect(
        self,
        pos_i: np.ndarray,
        pos_j: np.ndarray,
        type_i: int,
        type_j: int,
        max_distance: float,
    ) -> np.ndarray:
        """
        Returns a 2D vector (dx, dy) that can be added to velocity
        """
        strength = self.get_strength(type_i, type_j)
        # No intetaction if strength from the matrix
        if strength == 0:
            return np.zeros(2, dtype=float)

        delta = pos_j - pos_i
        dist = float(np.linalg.norm(delta))
        if dist == 0.0 or dist > max_distance:
            return np.zeros(2, dtype=float)

        direction = delta / dist
        # nearer = stronger
        falloff = 1.0 - (dist / max_distance)
        #return final interaction vector
        return direction * strength * falloff


