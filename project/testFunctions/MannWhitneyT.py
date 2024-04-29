import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the module from the parent package
from tests.MannWhitney import MannWhitney


if __name__ == '__main__':
    data1 = [5, 7, 3, 8, 6]
    data2 = [10, 12, 9, 11, 13]
    data=[data1,data2]
    mw = MannWhitney(data)
    mw.datacontroller()
    mw.steps()
    print("\n\n\n exemple du cahier")
    data1 = [2.1, 4.0, 6.3, 5.4, 4.8,3.7,6.1,3.3]
    data2 = [4.1, 0.6, 3.1, 2.5, 4.0 ,6.2 ,1.6 ,2.2 ,1.9, 5.4]
    data=[data1,data2]
    print(mw.formHyp())
    mw = MannWhitney(data)
    mw.datacontroller()
    mw.steps()
    mw.conclusion()


