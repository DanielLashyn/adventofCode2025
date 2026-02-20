#from Day2.main import main as Day2
from globalCode.classDayTemplate import DayTemplate
from globalCode.headerFileReader import *

test = DayTemplate(inputFileReader = fileReaderOneLineOneList())

test.displayIntro()
test.setData()
test.displayResult()
#Day2()
