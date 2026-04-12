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
        self.result = gridMap.getAccessableRolls()
        self.displayResult()

