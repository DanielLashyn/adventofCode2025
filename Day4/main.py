from globalCode.headerAll import *

class Day4(DayTemplate):

    def __init__(self,
                inputFileName = "input_real.txt",
                inputDifficulty = Diff.NORMAL):
        

        super().__init__(inputDay = 4, 
                    inputFileName = inputFileName,
                    inputFileReader = fileReaderMultiLine(),
                    inputDifficulty = inputDifficulty)

    def run(self):
        super().run()
        
       
        self.displayResult()

