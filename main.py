# This is the main file for running the Rachford-Rice contest.
# To learn more about how you can compete in the contest and where
# you have add your code, take a look at the "readme" file.

from time import perf_counter

import numpy as np
import pandas as pd

from check_convergence import is_converged
from rachford_rice_solution import racford_rice_solver

# (1) Read test cases for Rachford-Rice contest.
list_of_compositions = pd.read_csv("compositions.csv")
list_of_k_values = pd.read_csv("k-values.csv")

number_of_components = list_of_compositions.iloc[:, 0].to_list()
number_of_cases = len(number_of_components)
list_of_compositions = [
    list_of_compositions.iloc[n, 1 : Nc + 1].to_numpy()
    for n, Nc in enumerate(number_of_components)
]
list_of_k_values = [
    list_of_k_values.iloc[n, :Nc].to_numpy()
    for n, Nc in enumerate(number_of_components)
]

# Pre-allocate lists for summary and results files.
iterations = [0] * number_of_cases
vapor_compositions = [None] * number_of_cases
liquid_compositions = [None] * number_of_cases
vapor_fractions = [0] * number_of_cases
liquid_fractions = [0] * number_of_cases
sensitivities = [None] * number_of_cases
convergence_flags = [False] * number_of_cases  # False is fail and True is pass
run_time = 0

# (2) Iterate through, solve, and test each test case.
for n in range(number_of_cases):
    print("======================================================")
    print(f"Running case {n+1} of {number_of_cases}")

    Nc = int(number_of_components[n])
    compositions = list_of_compositions[n]
    k_values = list_of_k_values[n]

    # (2.1) Run Rachford-Rice solver (USER DEFINED FUCTION)
    t0 = perf_counter()
    (
        iterations[n],
        vapor_compositions[n],
        liquid_compositions[n],
        vapor_fractions[n],
        liquid_fractions[n],
    ) = racford_rice_solver(Nc, compositions, k_values)
    run_time += perf_counter() - t0

    # (2.2) Run tests on solver solutions
    sensitivities[n], convergence_flags[n] = is_converged(
        Nc,
        vapor_compositions[n],
        liquid_compositions[n],
        vapor_fractions[n],
        liquid_fractions[n],
        compositions,
        k_values,
        print_to_console=False
    )
    print(f"Did the case pass: {convergence_flags[n]}")

runs_failed = number_of_cases - np.count_nonzero(convergence_flags)

# (3) Print results and summary to output files.
with open("summary.txt", "w") as file:
    file.write("====================================================================\n")
    file.write("This is a summary of the calculations: \n")
    file.write("====================================================================\n")
    file.write(f"The program failed for {runs_failed} of {number_of_cases} runs!\n")
    file.write(f"The self reported number of iteration was {sum(iterations)}.\n")
    file.write(f"The average number of iterations was {sum(iterations)/number_of_cases}.\n")
    file.write(f"The total runtime was {np.round(run_time*1e3,2)} ms.")

with open("case-summary.txt", "w") as file:
    for i in range(number_of_cases):
        file.write(
            "====================================================================\n"
        )
        file.write(f"Case number: {i+1} \n")
        file.write(
            "====================================================================\n"
        )
        file.write(f"Did the case pass the test                : {convergence_flags[i]} \n")
        file.write(f"Sensitivity of the vapor composition test : {sensitivities[i][0]} \n")
        file.write(f"Sensitivity of the liquid composition test: {sensitivities[i][1]} \n")
        file.write(f"Sensitivity of the molar fraction test    : {sensitivities[i][2]} \n")
        file.write(f"Sensitivity of the material balance test  : {sensitivities[i][3]} \n")
        file.write(f"Sensitivity of the K-value test           : {sensitivities[i][4]} \n")
        file.write("==================================================================")

with open("case-summary-detailed.txt", "w") as file:
    for i in range(number_of_cases):
        file.write(
            "====================================================================\n"
        )
        file.write(f"Case number: {i+1} \n")
        file.write(
            "====================================================================\n"
        )
        file.write(f"Did the case pass the test                : {convergence_flags[i]} \n")
        file.write(f"Sensitivity of the vapor composition test : {sensitivities[i][0]} \n")
        file.write(f"Sensitivity of the liquid composition test: {sensitivities[i][1]} \n")
        file.write(f"Sensitivity of the molar fraction test    : {sensitivities[i][2]} \n")
        file.write(f"Sensitivity of the material balance test  : {sensitivities[i][3]} \n")
        file.write(f"Sensitivity of the K-value test           : {sensitivities[i][4]} \n")
        file.write("===== Detailed Data ===== \n")
        file.write(f"Vapor composition : {vapor_compositions[i]} \n")
        file.write(f"Liquid composition: {liquid_compositions[i]} \n")
        file.write(f"Vapor fraction : {vapor_fractions[i]} \n")
        file.write(f"Liquid fraction: {liquid_fractions[i]} \n")
        file.write("==================================================================")
