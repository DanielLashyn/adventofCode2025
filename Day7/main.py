from globalCode.headerAll import *
from .classes.tachyonDiagram import *

class Day7(DayTemplate):

    def __init__(self,
                inputFileName = "input_real.txt",
                inputDifficulty = Diff.NORMAL):
        

        super().__init__(inputDay = 7, 
                    inputFileName = inputFileName,
                    inputFileReader = fileReaderMultiLine(),
                    inputDifficulty = inputDifficulty)

    def run(self):
        super().run()

        diagram = tachyonDiagram()
        diagram.setDiagram(self.getData())
        diagram.display()
        self.result = 0
        self.displayResult()

