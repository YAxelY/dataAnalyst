import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the module from the parent package
from tests.AnovaOne import AnovaOne


if __name__ == '__main__':
    data1 = [5, 7, 3, 8, 6]
    data2 = [10, 12, 9, 11, 13]
    data =[data1,data2]
    an= AnovaOne(data)
    print(an.formHyp())
    print(an.N())


