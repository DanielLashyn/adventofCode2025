from globalCode.headerAll import *
from globalCode.classGridMap import *
from .classes.forkliftDiagram import *
class Day4(DayTemplate):

    def __init__(self,
                inputFileName = "input_real.txt",
                inputDifficulty = Diff.NORMAL):
        

        super().__init__(inputDay = 4, 
                    inputFileName = inputFileName,
                    inputFileReader = fileReaderMultiLineMultiOut(),
                    inputDifficulty = inputDifficulty)

    def run(self):
        super().run()
        gridMap = forkliftDiagram(self.getData())
        self.result = 0
        oldresult = - 1
        while oldresult != self.result:
            oldresult = self.result
            self.result = self.result + gridMap.getAccessableRolls(replace = True)        
        gridMap.display()
        self.displayResult()

