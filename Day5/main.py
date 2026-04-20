from globalCode.headerAll import *
from .classes.rangeList import *

class Day5(DayTemplate):

    def __init__(self,
                inputFileName = "input_real.txt",
                inputDifficulty = Diff.NORMAL):
        

        super().__init__(inputDay = 5, 
                    inputFileName = inputFileName,
                    inputFileReader = fileReaderMultiLineMultiOut(),
                    inputDifficulty = inputDifficulty)

    def run(self):
        super().run()
        ingredientIDRanges = rangeList()

        # TODO 
        # - Seperate the IDS and the ingredientIDRanges
        # - Add the Data to the ingredientIDRanges
        # - Loop through checking how many IDs are valid
        self.result = 0            

        self.displayResult()

