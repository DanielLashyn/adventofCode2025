from .ids import ids

class advanceIDs(ids):

    def _setInvalidID(self):
        self.invalidIDs = set()
        startLength = len(str(self.startID))
        endLength = len(str(self.endID))
       
        
        for curLength in range(1, endLength // 2 + 1):
            
            # Check if curLength is divisible within the range            
            if (startLength % curLength!= 0 and
                    endLength % curLength != 0):
                continue
                      
            for curID in range(self.startID, self.endID + 1):    
                
                if self._checkID(curID, curLength):
                    self.invalidIDs.add(curID)


    def _checkID(self, inID, curLength):
       
        strInID = str(inID)
        
        # Checks that it's a valid
        if (len(strInID) % curLength != 0):
            return False
        
        # Checks that it's not a single digit
        if len(strInID) <= 1:
            return False
    
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

