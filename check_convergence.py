from sys import float_info

import numpy as np

EPS_T = 1e-15
EPS_M = float_info.epsilon


def sensitivity(R: float, eps: float):
    return np.math.log10(R / eps) if R else -np.inf


def is_it_converged(test_sensitivity: float):
    return test_sensitivity <= 0


def phase_composition_test(ui: np.ndarray, Nc: int):
    eps_phase = EPS_T + Nc * EPS_M
    comp_sensitivity = sensitivity(abs(1 - np.sum(ui)), eps_phase)
    return comp_sensitivity, is_it_converged(comp_sensitivity)


def fraction_test(V: float, L: float):
    eps_f = EPS_T
    fraction_sensitivity = sensitivity(abs(V + L - 1) / (abs(V) + abs(L) + 1), eps_f)
    return fraction_sensitivity, is_it_converged(fraction_sensitivity)


def matbal_test(V: float, yi: np.ndarray, L: float, xi: np.ndarray, zi: np.ndarray):
    eps_z = EPS_T
    matbal_sensitivity = sensitivity(
        np.max(np.abs(V * yi + L * xi - zi) / (np.abs(V * yi) + np.abs(L * xi) + zi)), eps_z
    )
    return matbal_sensitivity, is_it_converged(matbal_sensitivity)


def k_value_test(yi: np.ndarray, xi: np.ndarray, Ki: np.ndarray):
    eps_k = EPS_T
    kvalue_sensitivity = sensitivity(
        np.max(np.abs(yi - Ki * xi) / (np.abs(yi) + np.abs(Ki * xi))), eps_k
    )
    return kvalue_sensitivity, is_it_converged(kvalue_sensitivity)


def inside_bounds(V: float, Ki: np.ndarray):
    Vmin = 1 / (1 - np.max(Ki))
    Vmax = 1 / (1 - np.min(Ki))
    return V < Vmax and Vmin < V


def is_converged(
    Nc: int,
    yi: np.ndarray,
    xi: np.ndarray,
    V: float,
    L: float,
    zi: np.ndarray,
    Ki: np.ndarray,
    print_to_console: bool = False
):
    vap_comp_sensitivity, is_vap_comp_converged = phase_composition_test(yi, Nc)
    liq_comp_sensitivity, is_liq_comp_converged = phase_composition_test(xi, Nc)
    fraction_sensitivity, is_fraction_converged = fraction_test(V, L)
    matbal_sensitivity, is_matbal_converged = matbal_test(V, yi, L, xi, zi)
    kvalue_sensitivity, is_kvalue_converged = k_value_test(yi, xi, Ki)

    if print_to_console:
        print("==================================================================")
        print(f"Did the vapor composition test converge : {is_vap_comp_converged}")
        print(f"Did the liquid composition test converge: {is_liq_comp_converged}")
        print(f"Did the molar fraction test converge    : {is_fraction_converged}")
        print(f"Did the material balance test converge  : {is_matbal_converged}")
        print(f"Did the K-value test converge           : {is_kvalue_converged}")
        print(f"Was the solution within the bounds      : {inside_bounds(V, Ki)}")
        print("==================================================================\n")

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
