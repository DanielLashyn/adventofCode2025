from pathlib import Path
from platform import system
from globalCode.enums import Difficulty as diff
from globalCode.headerFileReader import *

class DayTemplate():


    def __init__(self, 
                inputDay = 0,
                inputFileName = "input_real.txt", 
                inputFileReader = interfaceFileReader(),
                inputDifficulty = diff.NORMAL):
        
        self.difficulty = inputDifficulty
        self.fileName = inputFileName
        self.day = inputDay
        self.filePath = self._getFilePath() + str(inputFileName)
        self.fileReader = inputFileReader
        self.result = 0


    def run(self):
        self.displayIntro()
        self.setData()

    def displayIntro(self):
        print("**************************")
        print("Advent Day " + str(self.day))
        print("Data used: " + str(self.fileName))
        print("Puzzle mode: " + str(self.difficulty.name))
        print("**************************")

    def setData(self): 
        self.fileReader.setData(self.filePath)

    def getData(self):
        return self.fileReader.getData()

    def displayResult(self):
        print("Result: " + str(self.result))

    def _getFilePath(self):
        
        # Gets the correct slash for the OS
        osName = str(system())
        if osName == "Windows":
            slash = '\\'
        else:
            slash = '/'
        # Gets the path
        path = str(Path(__file__).resolve().parent)
        path = path.replace("globalCode", "Day" + str(self.day) + str(slash))
       
        return path

