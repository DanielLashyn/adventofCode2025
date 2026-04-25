from globalCode.headerAll import *
from .classes.rangeList import *

class Day5(DayTemplate):

    def __init__(self,
                inputFileName = "input_real.txt",
                inputDifficulty = Diff.NORMAL):
        

        super().__init__(inputDay = 5, 
                    inputFileName = inputFileName,
                    inputFileReader = fileReaderMultiLine(),
                    inputDifficulty = inputDifficulty)

    def run(self):
        super().run()
        ingredientIDRanges = rangeList()

        isIngredient = False
        freshIngredients = 0
        freshRanges = 0
        for item in self.getData():
            
            # Checks if the list is switching from ranges to ingredient
            if (item == ""):
                isIngredient = True
                continue

            if (isIngredient):
                if (ingredientIDRanges.itemInRange(item)):
                    freshIngredients = freshIngredients + 1
            else:
                ingredientIDRanges.addRange(item)
        freshRanges = ingredientIDRanges.countTotalRanges()
        
        self.result = freshIngredients if self.difficulty == Diff.NORMAL else freshRanges

        self.displayResult()

