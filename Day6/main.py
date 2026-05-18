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

        for line in self.getData():
            line = line.split()
            print(line)


        self.result = 0


        self.displayResult()

