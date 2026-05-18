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

        equations = equationList()
        equations.initData(self.getData())
        self.result = equations.getResult()
        self.displayResult()

