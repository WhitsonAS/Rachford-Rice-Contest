# This is the main file for running the Rachford-Rice contest.
# To learn more about how you can compete in the contest and where
# you have add your code, take a look at the "readme" file.

import pandas as pd
import numpy as np

from rachford_rice_solution import racford_rice_solver

# (1) Read test cases for Rachford-Rice contest.
list_of_compositions = pd.read_csv("compositions.csv")
list_of_k_values = pd.read_csv("k-values.csv")
number_of_components = list_of_compositions.iloc[:, 0].to_list()
number_of_cases = len(number_of_components)
list_of_compositions = [
    [zi for zi in list_of_compositions.iloc[n, 1:].to_list() if str(zi) != "nan"]
    for n in range(number_of_cases)
]
list_of_k_values = [
    [Ki for Ki in list_of_k_values.iloc[n, :].to_list() if str(Ki) != "nan"]
    for n in range(number_of_cases)
]

# Pre-allocate lists for summary and results files.
iterations = [0] * number_of_cases
vapor_compositions = [0] * number_of_cases
liquid_compositions = [0] * number_of_cases
vapor_fractions = [0] * number_of_cases
liquid_fractions = [0] * number_of_cases
sensitivities = [0] * number_of_cases
convergence_flags = [False] * number_of_cases  # False is fail and True is pass

# (2) Iterate through, solve, and test each test case.
for n in range(number_of_cases):
    # (2.1) Make list into numpy array
    Nc = int(number_of_components[n])
    compositions = np.array(list_of_compositions[n])
    k_values = np.array(list_of_k_values[n])

    # (2.2) Run Rachford-Rice solver (USER DEFINED FUCTION)
    [
        iterations[n],
        vapor_compositions[n],
        liquid_compositions[n],
        vapor_fractions[n],
        liquid_fractions[n],
    ] = racford_rice_solver(Nc, compositions, k_values)

    # (2.3) Run tests on solver solutions


# (3) Print results and summary to output files.
