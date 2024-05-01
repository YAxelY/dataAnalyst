22/04/2024 13:36

what I've done:
- created a virtual environment for windows users maned "vendata" using `python -m venv vendata`
- installed a new packages named "scipy" using `pip install scipy`
- created a new class named "MannWhitney.py"  within project/tests


Instructions
on windows:
 1. pull the project from the branch develop  using `git pull origin develop`
 2. run `venv\Scripts\activate` from within the project root directory to activate the virtual environment

 on linux:
  1. one might create  a virtual environment for linux named "vendataL" using `python3 -m venv vendataL` fron within the run directory of the project
  2.  run `source venv/bin/activate` from within the project root directory to activate the virtual envrironment

What I'm doing:

- implementing the MannWhitney test and of course providing testvalues for that test.


24/04/2024 04:26

what I've done:
- created a virtual environment for linux users maned "vendataL" using `python3 -m venv vendataL`


from 27/04/2024 till 29/04/2024 

what I've done:

  - I've partly completed the GUI

Instructions:

  if you wanna integrate your  completed test do as follow:

  1. first let's ensure that your test follow this struture :

     from scipy.stats import kruskal, chi2  # import all the necessary packages as will

        class Name:
      # commun functions !! you must strictly respect these interfaces and each commun functions should return a string as result.
            def __init__(self,dataSet):
                
                
            def datacontroller(self):
              
            
            def formHyp(self):

            
            def distribution(self):
                
            def testval(self):
                
            
            def steps(self,alpha):

                alpha = float(alpha)

                
            def conclusion(self,alpha = 0.05,desc=""):

                alpha = float(alpha)
                desc= str(desc)

          # definition optionnelle , this functions should return all the widgets used to create your own data input .

            def dataEntry(self):
               

             
          # personnal function , these are personnal functions and you might define them as you want (they will only be used within this class)
            def myFunction(myArg1,myArg2,...):
  
  2. now follow these steps to integrate it to the GUI

      - Add a new menu to test_menu as follow  in App.py:
            - key in crtl +f and search for "test_menu " add this line at the bottom    
            self.test_menu.add_command(label="Gui test Name", command=lambda: self.select_test("className"))   
      - now modify self.select_test function as follow
            - key n crtl+f and search for "select_test" add this line at the right place
            if self.selectedTest=="className":
            self.currentTest=className(self.data)

  3. if everything okay, you are done for thank you for contributing , please don't forget to test out.





  

