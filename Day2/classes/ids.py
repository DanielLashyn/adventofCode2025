class ids:
    def __init__(self, idRanges):
        # gets the range of the id 
        splitRanges = idRanges.split('-')

        # Check that only 2 ids are passed through
        if len(splitRanges)  != 2:
            print("Error: Not valid Range, please format as 'startID-EndID'")
            self.setStartID("not Valid")
            self.setEndID("not Valid")
        else:
            self.setStartID(splitRanges[0])
            self.setEndID(splitRanges[1])

    # Getters and setters for startID and endID
    def setStartID(self, passID):
        self.startID = self._getValidID(passID)

    def getStartID(self):
        return self.startID

    def setEndID(self, passID):
        self.endID = self._getValidID(passID)

    def getEndID(self):
        return self.endID

    # Checks that the values for startID and endID are valid
    def _getValidID(self, passID):

        if isinstance(passID, str) and passID.isdigit():
            return int(passID)

        elif isinstance(passID, int):
            return passID

        else:
            print("Error: Not valid ID")
            return -1



    # Displays information about this class
    def display(self):
        print("Start ID: " + str(self.startID))
        print("End ID: "   + str(self.endID)  )

