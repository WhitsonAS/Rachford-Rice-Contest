import pandas as pd
import numpy as np
from typing import List
from sys import float_info

EPS_T = 1e-15
EPS_M = float_info.epsilon
print(EPS_M)


def sensitivity(R: float, eps: float):
    return np.math.log10(R / eps)


def is_it_converged(test_sensitivity: float):
    return test_sensitivity < 0


def phase_composition_test(ui: np.array, Nc: int):
    eps_phase = EPS_T + Nc * EPS_M
    comp_sensitivity = sensitivity(abs(1 - np.sum(ui)), eps_phase)
    return comp_sensitivity, is_it_converged(comp_sensitivity)


def fraction_test(V: float, L: float):
    eps_f = EPS_T
    fraction_sensitivity = sensitivity(abs(V + L - 1) / (abs(V) + abs(L) + 1), eps_f)
    return fraction_sensitivity, is_it_converged(fraction_sensitivity)


def matbal_test(V: float, yi: np.array, L: float, xi: np.array, zi: np.array):
    eps_z = EPS_T
    matbal_sensitivity = sensitivity(
        np.max(abs(V * yi + L * xi - zi) / (abs(V * yi) + abs(L * xi) + zi)), eps_z
    )
    return matbal_sensitivity, is_it_converged(matbal_sensitivity)


def k_value_test(yi: np.array, xi: np.array, Ki: np.array):
    eps_k = EPS_T
    kvalue_sensitivity = sensitivity(
        np.max(abs(yi + Ki * xi) / (abs(yi) + abs(Ki * xi))), eps_k
    )
    return kvalue_sensitivity, is_it_converged(kvalue_sensitivity)


def inside_bounds(V: float, Ki: np.array):
    Vmin = 1 / (1 - np.max(Ki))
    Vmax = 1 / (1 - np.min(Ki))
    return V < Vmax and Vmin < V


def is_converged(
    Nc: int,
    yi: np.array,
    xi: np.array,
    V: float,
    L: float,
    zi: np.array,
    Ki: np.array,
):
    vap_comp_sensitivity, is_vap_comp_converged = phase_composition_test(yi, Nc)
    liq_comp_sensitivity, is_liq_comp_converged = phase_composition_test(xi, Nc)
    fraction_sensitivity, is_fraction_converged = fraction_test(V, L)
    matbal_sensitivity, is_matbal_converged = matbal_test(V, yi, L, xi, zi)
    kvalue_sensitivity, is_kvalue_converged = k_value_test(yi, zi, Ki)

    check_if_converged = (
        is_vap_comp_converged
        and is_liq_comp_converged
        and is_fraction_converged
        and is_matbal_converged
        and is_kvalue_converged
        and inside_bounds(V, Ki)
    )

    sensitivities = [
        vap_comp_sensitivity,
        liq_comp_sensitivity,
        fraction_sensitivity,
        matbal_sensitivity,
        kvalue_sensitivity,
    ]
    return sensitivities, check_if_converged
