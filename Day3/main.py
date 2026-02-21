from globalCode.headerAll import *
from .classes.bank import Bank

class Day3(DayTemplate):

    def __init__(self,
                inputFileName = "input_real.txt",
                inputDifficulty = Diff.NORMAL):
        

        super().__init__(inputDay = 3, 
                    inputFileName = inputFileName,
                    inputFileReader = fileReaderMultiLine(),
                    inputDifficulty = inputDifficulty)

    def run(self):
        #super().run()
        test = Bank(2452532)
        #rawData = self.getData()
        pass
