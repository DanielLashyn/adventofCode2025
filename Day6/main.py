from globalCode.headerAll import *
from .classes.equation import *
from .classes.equationList import *

class Day6(DayTemplate):

    def __init__(self,
                inputFileName = "input_real.txt",
                inputDifficulty = Diff.NORMAL):
        

        super().__init__(inputDay = 6, 
                    inputFileName = inputFileName,
                    inputFileReader = fileReaderMultiLine(),
                    inputDifficulty = inputDifficulty)

    def run(self):
        super().run()

        #equations = []
        currentLine = 0


        equations = equationList()
        equations.initData(self.getData())
        equations.display()
        
        
        # Loops through all the data
        """for line in self.getData():
            currentLine += 1
            line = line.split()
            print(line)
    
            for item in line:

                if currentLine == 1:
                    temp = equation()
                    temp.append(item)
                    equations.append(temp)

        print(equations[0].display())
        """
        self.result = 0


        self.displayResult()

