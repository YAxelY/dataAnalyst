import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.Chi2 import Chi2

if __name__ == '__main__':
    data1 = [10, 20, 30, 15]
    data2 = [25, 15, 30, 40, 50]
    dataSet = [data1,data2]
    
    ch = Chi2(dataSet)
    print(ch.formHyp())
    ch.steps(0.05)
    
    
