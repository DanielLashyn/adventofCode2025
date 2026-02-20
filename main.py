from Day2.main import * 
from globalCode.classDayTemplate import DayTemplate
from globalCode.headerFileReader import *
'''
test = DayTemplate(inputFileReader = fileReaderOneLine())

test.displayIntro()
test.setData()
test.displayResult()
'''
tester = Day2(inputFileName = "input_real.txt", 
        inputDifficulty = Diff.ADVANCE)
tester.run()

