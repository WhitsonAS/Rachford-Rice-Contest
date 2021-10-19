from typing import Tuple

import numpy as np
from check_convergence import EPS_T

MAX_ITR = 100


def rachford_rice_solver(
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
    K_max = np.max(Ki)
    K_min = np.min(Ki)
    V_min = 1 / (1 - K_max)
    V_max = 1 / (1 - K_min)

    def rr(V: float) -> float:
        return np.dot(zi, (Ki - 1) / (1 + V * (Ki - 1)))

    def drr(V: float) -> float:
        return -np.dot(zi, ((Ki - 1) / (1 + V * (Ki - 1))) ** 2)

    V = (V_min + V_max) / 2
    h = np.inf

    Niter = 0

    while abs(h) > EPS_T:
        Nc += 1

        h = rr(V)
        dh = drr(V)

        if h > 0:
            V_min = V
        else:
            V_max = V

        V = V - h / dh

        if V < V_min or V > V_max:
            V = (V_max + V_min) / 2

        if Niter > MAX_ITR:
            break

    L = 1 - V
    xi = zi / (1 + V * (Ki - 1))
    yi = Ki * xi

    return Niter, yi, xi, V, L
