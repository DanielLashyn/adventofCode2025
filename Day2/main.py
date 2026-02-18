from pathlib import Path
from globalClasses.enums import Difficulty
from .classes.ids import ids
from .classes.advanceIDs import advanceIDs

def main():
    selectDifficulty = Difficulty.ADVANCE

    idList = []
    fileData = "input_example.txt"

    print("Day 2:")
    print("Using Data from " + fileData)
    filePath = str(Path(__file__).resolve().parent) + "/" + fileData

    # Gets the raw data from the text file
    with open(filePath, "r") as file:
        rawData = file.readline().rstrip("\n")
        rawData = rawData.split(',')

    # Sets the object type based on the puzzle difficulty
    idsConstruct = ids if selectDifficulty == Difficulty.NORMAL else advanceIDs 


    idList = [idsConstruct(data) for data in rawData]
    total = sum(ids.sumIDs() for ids in idList)

    #[ids.display() for ids in idList]

    print("Total valid IDS: "+ str(total))


if __name__ == "__main__":
    main()
