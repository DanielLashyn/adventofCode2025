from .classes.ids import ids
from .classes.advanceIDs import advanceIDs
from globalCode.headerAll import *

class Day2(DayTemplate):

    def __init__(self,
                inputFileName = "input_real.txt",
                inputDifficulty = Diff.NORMAL):
        

        super().__init__(inputDay = 2, 
                    inputFileName = inputFileName,
                    inputFileReader = fileReaderOneLine(delimiter = ','),
                    inputDifficulty = inputDifficulty)

    def run(self):
        super().run()

        rawData = self.getData()
        idList = []
    

        # Sets the object type based on the puzzle difficulty
        idsConstruct = ids if self.difficulty == Diff.NORMAL else advanceIDs 


        idList = [idsConstruct(data) for data in rawData]
        total = sum(ids.sumIDs() for ids in idList)

    #[ids.display() for ids in idList]

        print("Total valid IDS: "+ str(total))
