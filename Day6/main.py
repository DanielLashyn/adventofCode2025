from globalCode.headerAll import *
from .classes.equation import *

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

        equations = []
        currentLine = 0
        for line in self.getData():
            currentLine += 1
            line = line.split()

            for item in line:
                print(item)

                if currentLine == 1:
                    temp = equation()
                    temp.append(item)
                    equations.append(temp)

        #print(equations[0].display())
        
        self.result = 0


        self.displayResult()

