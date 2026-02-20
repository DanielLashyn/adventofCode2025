from globalCode.enums import Difficulty

class DayTemplate():

    def __init__(self, 
                inputDay = 0,
                inputFileName = "input_real.txt", 
                inputDifficulty = "NORMAL"):
        
        self.difficulty = inputDifficulty
        self.FileName = inputFileName
        self.FilePath = "Blah" + "\\" + str(inputFileName) 
        self.curDay = inputDay
        self.result = 0
        
    def displayIntro(self):
        print("**************************")
        print("Advent Day " + str(self.curDay))
        print("Data used: " + str(self.FilePath))
        print("Puzzle mode:" + str(self.difficulty))
        print("**************************")


    def displayResults(self):
        print("Result: " + str(result))




