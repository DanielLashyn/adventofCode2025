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
    
                self._checkID(121212, 2)
                self.invalidIDs.append(curID)


    def _checkID(self, inID, curLength):
       
        strInID = str(inID)
        startSection = 0
        endSection = 0
        matchSection = strInID[0:curLength]


        for curSection in range(1, len(strInID)//curLength + 1):
            endSection += curLength
            slicedSection = strInID[startSection:endSection]
            if slicedSection != matchSection:
                return False

            startSection += curLength


        # Gets here means the ID matches
        return True     

