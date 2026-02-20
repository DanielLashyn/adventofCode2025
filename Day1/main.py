from globalCode.headerAll import *
from .classes.rotation import rotation
from .classes.dial import Dial

class Day1(DayTemplate):

    def __init__(self,
                inputFileName = "input_real.txt",
                inputDifficulty = Diff.NORMAL):
        

        super().__init__(inputDay = 1, 
                    inputFileName = inputFileName,
                    inputFileReader = fileReaderMultiLine(),
                    inputDifficulty = inputDifficulty)

    def run(self):
        super().run()

      
        instructions = []
        dial = Dial()
        
        rawData = self.getData()

        # Converts the raw data into the rotation class
        for data in rawData:
            rotationData = rotation(data)
            instructions.append(rotationData)

        for rotationData in instructions:
            dial.updatePostion(rotationData)

        dial.printValues()
