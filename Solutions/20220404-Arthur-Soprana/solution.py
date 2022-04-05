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
    from sys import float_info
    EPS_M = float_info.epsilon

    K_max = np.max(Ki)
    K_min = np.min(Ki)
    V_min = 1 / (1 - K_max)
    V_max = 1 / (1 - K_min)

    def rr(V: float) -> float:
        return np.sum(zi * (Ki - 1) / (1 + V * (Ki - 1)))

    def drr(V: float) -> float:
        factor = (Ki - 1) / (1 + V * (Ki - 1))
        return -np.sum(zi * factor * factor)

    V = 0.5 * (V_min + V_max)
    h = np.inf

    Niter = 0

    while abs(h) > EPS_T:
        Niter += 1

        h = rr(V)
        dh = drr(V)

        if h > 0:
            V_min = V
        else:
            V_max = V

        V = V - h / dh

        if V < V_min or V > V_max:
            V = 0.5 * (V_max + V_min)

        if Niter > 100:
            break

    def calculate_L_handling_degenerate_case(V: float, threshold: float = 1e-12) -> float:
        """
        The special treatment inside this method is required here in order to handle
        degenerate case 1.
        """
        L = 1 - V
        if abs(L) < threshold:
            return (1.0 - (L + V)) + threshold
        return L

    L = calculate_L_handling_degenerate_case(V)

    ci = 1.0 / (Ki - 1.0)
    xi = 1.0 / (1.0 / zi + V / (ci * zi))  # == zi / (1 + V * (Ki - 1))
    yi = Ki * xi

    idx_liq = np.argmax(xi)
    idx_vap = np.argmax(yi)

    xi_sum_residual = 1.0 - xi.sum()
    if abs(xi_sum_residual) > EPS_T + Nc * EPS_M:
        xi[idx_liq] += xi_sum_residual
        yi[idx_liq] += Ki[idx_liq] * xi_sum_residual

    mass_balance_residual = V * yi + L * xi - zi
    residual_ratio = np.abs(mass_balance_residual) / (np.abs(V * yi) + np.abs(L * xi) + zi)
    delta = mass_balance_residual / (V * (Ki - 1.0) + 1.0)
    xi = np.where(residual_ratio > EPS_T, xi - delta, xi)
    yi = Ki * xi

    yi_sum_residual = 1.0 - yi.sum()
    if abs(yi_sum_residual) > EPS_T + Nc * EPS_M:
        xi[idx_vap] += yi_sum_residual / Ki[idx_vap]
        yi[idx_vap] += yi_sum_residual

    return Niter, yi, xi, V, L
