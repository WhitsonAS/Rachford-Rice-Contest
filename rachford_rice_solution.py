from typing import Tuple

import numpy as np

EPS_T = 1e-15
MAX_ITR = 100


def racford_rice_solver(
    Nc: int, zi: np.ndarray, Ki: np.ndarray
) -> Tuple[int, np.ndarray, np.ndarray, float, float]:
    """
    This function solves for the root of the Rachford-Rice equation. The solution
    is defined by the contestent and this is the only part of the code that the
    contestent should change.

    The input is the number of components (Nc), the total composition (zi), and the K-values (KI).

    The output is the number of iterations used (N), the vapor molar composition (yi), the liquid
    molar composition (xi), the vapor molar fraction (V), and the liquid molar fraction (L).
    """
    # ===== Add your code below (remember to remove the dummy variables). ===== 



    # ===== REMOVE DUMMY VALUES BELOW =====
    N = 1
    yi = np.array([0])
    xi = np.array([0])
    V = 0
    L = 0
    # =====================================
    if N >= MAX_ITR:
        print("******************************************************")
        print("*** The maximum number of iterations was exceeded! ***")
        print("******************************************************")

    return N, yi, xi, V, L
