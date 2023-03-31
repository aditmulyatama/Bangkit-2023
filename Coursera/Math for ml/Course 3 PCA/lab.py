import numpy as np
# GRADED FUNCTION: DO NOT EDIT THIS LINE


def projection_matrix_1d(b):
    """Compute the projection matrix onto the space spanned by `b`
    Args:
        b: ndarray of dimension (D,), the basis for the subspace

    Returns:
        P: the projection matrix
    """
    # YOUR CODE HERE
    # Uncomment and modify the code below
    D = b.shape[0]
    # Compute the outer product of b with itself
    bbT = np.outer(b, b)
    # Compute the scalar denominator of the projection formula
    bTb = np.linalg.norm(b)**2
    # Compute the projection matrix as (bb^T) / (b^Tb)
    P = bbT / bTb
    return P
# GRADED FUNCTION: DO NOT EDIT THIS LINE


def project_1d(x, b):
    """Compute the projection matrix onto the space spanned by `b`
    Args:
        x: the vector to be projected
        b: ndarray of dimension (D,), the basis for the subspace

    Returns:
        y: ndarray of shape (D,) projection of x in space spanned by b
    """
    # YOUR CODE HERE
    # Uncomment and modify the code below
    p = np.outer(b, b)/(np.linalg.norm(b)**2) @ x  # <-- EDIT THIS
    return p
