import numpy as np


class Interaction:
    """
    Stores and manages the interaction matrix between particle types.

    The matrix defines attraction (positive values) and repulsion
    (negative values) between different particle types.
    """

    def __init__(self, matrix: np.ndarray | None = None):
        """
        Initialize the interaction matrix.

        Parameters
        ----------
        matrix : np.ndarray | None, optional
            Custom interaction matrix. If None, a default 4x4
            interaction matrix is used.
        """
        if matrix is None:
            matrix = np.array([
                [ 0.2,  0.5, -0.4,  0.0],
                [-0.2,  0.2,  0.5, -0.4],
                [-0.4, -0.2,  0.2,  0.5],
                [ 0.5, -0.4, -0.2,  0.2],
            ], dtype=float)

        self.matrix = matrix.astype(float)

    def get_strength(self, type_i: int, type_j: int) -> float:
        """
        Return the interaction strength between two particle types.

        Parameters
        ----------
        type_i : int
            Type of the source particle.
        type_j : int
            Type of the target particle.

        Returns
        -------
        float
            Interaction strength stored at matrix[type_i, type_j].
        """
        return float(self.matrix[type_i, type_j])
