from .ids import ids

class advanceIDs(ids):

    def _setInvalidID(self):
        self.invalidIDs = []
        startLength = len(str(self.startID))
        endLength = len(str(self.startID))
        self.invalidIDs.append(endLength)
        
        for curLength in range(1, endLength // 2 + 1):
            self.invalidIDs.append(curLength)   
            #middle = len(curStr)//2
            #startHalf = curStr[0:middle]
            #endHalf = curStr[middle:]


