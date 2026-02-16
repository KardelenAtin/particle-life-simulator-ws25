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

    