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
        super().run()
        
        batteryBanks = []
        self.result = 0
        for data in self.getData():
            batteryBanks.append(Bank(data))

        for bank in batteryBanks:
            bank.findMaxVoltage()
            self.result = self.result + bank.getMaxVoltage()            


        self.displayResult()

