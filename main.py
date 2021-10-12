# This is the main file for running the Rachford-Rice contest.
# To learn more about how you can compete in the contest and where
# you have add your code, take a look at the "readme" file.

import pandas as pd
import numpy as np

from time import perf_counter
from rachford_rice_solution import racford_rice_solver
from check_convergence import is_converged

# (1) Read test cases for Rachford-Rice contest.
list_of_compositions = pd.read_csv("compositions.csv")
list_of_k_values = pd.read_csv("k-values.csv")
number_of_components = list_of_compositions.iloc[:, 0].to_list()
number_of_cases = len(number_of_components)
list_of_compositions = [
    list_of_compositions.iloc[n, 1 : number_of_components[n] + 1].to_list()
    for n in range(number_of_cases)
]
list_of_k_values = [
    list_of_k_values.iloc[n, : number_of_components[n]].to_list()
    for n in range(number_of_cases)
]

# Pre-allocate lists for summary and results files.
iterations = [0] * number_of_cases
vapor_compositions = [0] * number_of_cases
liquid_compositions = [0] * number_of_cases
vapor_fractions = [0] * number_of_cases
liquid_fractions = [0] * number_of_cases
sensitivities = [[0] * 5] * number_of_cases
convergence_flags = [False] * number_of_cases  # False is fail and True is pass
run_time = 0

# (2) Iterate through, solve, and test each test case.
for n in range(number_of_cases):
    # (2.1) Make list into numpy array
    Nc = int(number_of_components[n])
    compositions = np.array(list_of_compositions[n])
    k_values = np.array(list_of_k_values[n])

    # (2.2) Run Rachford-Rice solver (USER DEFINED FUCTION)
    t0 = perf_counter()
    [
        iterations[n],
        vapor_compositions[n],
        liquid_compositions[n],
        vapor_fractions[n],
        liquid_fractions[n],
    ] = racford_rice_solver(Nc, compositions, k_values)
    run_time += perf_counter() - t0

    # (2.3) Run tests on solver solutions
    sensitivities[n], convergence_flags[n] = is_converged(
        Nc,
        vapor_compositions[n],
        liquid_compositions[n],
        vapor_fractions[n],
        liquid_fractions[n],
        compositions,
        k_values,
    )
    runs_failed = sum(np.array(convergence_flags) == False)


# (3) Print results and summary to output files.
with open("summary.txt", "w") as file:
    file.write("====================================================================\n")
    file.write("This is a summary of the calculations: \n")
    file.write("====================================================================\n")
    file.write(f"The program failed for {runs_failed} of {number_of_cases} runs!\n")
    file.write(f"The self reported number of iteration was {sum(iterations)}.\n")
    file.write(f"The total runtime was {np.round(run_time*1e6,2)} μs.")