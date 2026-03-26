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
        testGridData = self.getData()
        print(testGridData)
        testGridMap = forkliftDiagram(testGridData)
        testGridMap.display()
        testGridMap.displaySection((1,3), (1,3))
        testGridMap.countCharInSection((6,0), 
            wantedChar = '@', 
            distanceFromCenter = 1)
        testGridMap.getAccessableRolls()

        #self.displayData() 
       
        #self.displayResult()

