import sys
import os

import numpy as np

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tests.Chi2Homogeneity import ChiSquareHomogeneityTest


if "__name__" == "__main__":

    observed_data = np.array([[10, 20, 30], [15, 25, 35], [20, 30, 40]])
    chi_square_test = ChiSquareHomogeneityTest(observed_data)
    print(chi_square_test.formHyp())
    print(chi_square_test.distribution())
    print(chi_square_test.steps(0.05))
    print(chi_square_test.conclusion())