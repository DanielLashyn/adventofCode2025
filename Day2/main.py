from pathlib import Path
#from globalClasses.enums import Difficulty
from .classes.ids import ids
from .classes.advanceIDs import advanceIDs

def main():
    idList = []
    fileData = "input_real.txt"

    print("Day 2:")
    print("Using Data from " + fileData)
    filePath = str(Path(__file__).resolve().parent) + "/" + fileData

    # Gets the raw data from the text file
    with open(filePath, "r") as file:
        rawData = file.readline().rstrip("\n")
        rawData = rawData.split(',')

    idsConstruct = advanceIDs

    idList = [idsConstruct(data) for data in rawData]
    total = sum(ids.sumIDs() for ids in idList)

    idList[1].display()
    print("Total valid IDS: "+ str(total))


if __name__ == "__main__":
    main()
