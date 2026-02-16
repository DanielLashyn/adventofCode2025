class ids:
    def __init__(self, idRanges):
        # gets the range of the id 
        splitRanges = idRanges.split('-')
        self.validIDs = []
        self.IDsSum = 0

        # Check that only 2 ids are passed through
        if len(splitRanges)  != 2:
            print("Error: Not valid Range, please format as 'startID-EndID'")
            self.setStartID("not Valid")
            self.setEndID("not Valid")
        else:
            self.setStartID(splitRanges[0])
            self.setEndID(splitRanges[1])
            self._setValidID()

    # Getters and setters for startID and endID
    def setStartID(self, passID):
        self.startID = self._getValidID(passID)

    def getStartID(self):
        return self.startID

    def setEndID(self, passID):
        self.endID = self._getValidID(passID)

    def getEndID(self):
        return self.endID

    def _setValidID(self):
        
        self.validIDs = []
        for curInt in range(self.startID, self.endID + 1):
            curStr = str(curInt)
            
            # Skips if the length is odd, as we don't need to check
            if len(curStr) %2 != 0:
                continue

            middle = len(curStr)//2
            startHalf = curStr[0:middle]
            endHalf = curStr[middle:]
        
            if startHalf == endHalf:
                self.validIDs.append(curInt)

    # Checks that the values for startID and endID are valid
    def _getValidID(self, passID):

        if isinstance(passID, str) and passID.isdigit():
            return int(passID)

        elif isinstance(passID, int):
            return passID

        else:
            print("Error: Not valid ID")
            return -1

    def hasValidIDs(self):
        return len(self.validIDs) != 0

    # Displays information about this class
    def display(self, displayIfNoIDs = True):
       
        if not displayIfNoIDs and not self.hasValidIDs():
            return

        print("ID Range: " + str(self.startID)  + "-" + str(self.endID))
        self.displayValidIDs()
        print("Sum of Valid IDs: "+ str(self.sumIDs()))

    def displayValidIDs(self):
        if not self.hasValidIDs():
            print("No Valid IDs")
        else:
            print("Valid ID: " + str(self.validIDs) )

    def sumIDs(self):
        if not self.hasValidIDs():
            return 0
        else:
            return sum(self.validIDs)
           
