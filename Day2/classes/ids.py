class ids:
    def __init__(self, idRanges):
        self.setStartID(idRanges)
        self.setEndID(idRanges)

    def setStartID(self, passID):
        self.startID = self.getValidID(passID)

    def setEndID(self, passID):
        self.endID = self.getValidID(passID)

    def getValidID(self, passID):

        if isinstance(passID, str) and passID.isdigit():
            return int(passID)

        elif isinstance(passID, int):
            return passID

        else:
            print("Error: Not valid start id")
            return -1



    def display(self):
        print("Start ID: " + str(self.startID))
        print("End ID: "   + str(self.endID)  )

