from globalCode.enums import Difficulty as diff

class DayTemplate():

    def __init__(self, 
                inputDay = 0,
                inputFileName = "input_real.txt", 
                inputDifficulty = diff.NORMAL):
        
        self.difficulty = inputDifficulty
        self.fileName = inputFileName
        self.filePath = "Blah" + "\\" + str(inputFileName) 
        self.curDay = inputDay
        self.result = 0
        
    def displayIntro(self):
        print("**************************")
        print("Advent Day " + str(self.curDay))
        print("Data used: " + str(self.fileName))
        print("Puzzle mode: " + str(self.difficulty.name))
        print("**************************")

    def setData(self):
        print("Method stub to set data")

    def displayResult(self):
        print("Result: " + str(self.result))




