from globalCode.headerAll import *
from .classes.bank import Bank
from .classes.advanceBank import AdvanceBank as advBank

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
        
        bankConstruct = Bank if self.difficulty == Diff.NORMAL else advBank 

        for data in self.getData():
            batteryBanks.append(bankConstruct(data))

        for bank in batteryBanks:
            bank.findMaxVoltage()
            self.result = self.result + bank.getMaxVoltage()            


        self.displayResult()

