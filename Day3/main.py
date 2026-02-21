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
        test = Bank(8765432111119)
        print(test.findMaxVoltage())
        print(test.getMaxVoltage())
        #rawData = self.getData()
        pass
