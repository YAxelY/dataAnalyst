import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the module from the parent package
from tests.Wilcoxon import WilcoxonTest

if __name__ == "__main__":
    dataSet = ([9, 10, 11, 10, 14, 15, 18, 10, 14, 12], [8, 10, 12, 9, 17, 13, 15, 11, 14, 10])
    wc = WilcoxonTest(dataSet, test_type="two-sided")
    wc.formHyp()
    wc.distribution()
    wc.testval()
    wc.steps()
    wc.conclusion()