from .ids import ids

class advanceIDs(ids):

    def _setInvalidID(self):
        self.invalidIDs = []
        startLength = len(str(self.startID))
        endLength = len(str(self.startID))
        self.invalidIDs.append(endLength)
        
        for curLength in range(1, endLength // 2 + 1):
           
            # Check if curLength is divisible within the range
            if ((startLength - endLength) < 2 and
                    startLength % curLength!= 0 and
                    endLength % curLength != 0):
                continue
            self.invalidIDs.append(curLength)
            
            for curID in range(self.startID, self.endID + 1):
                self.invalidIDs.append(curID)
