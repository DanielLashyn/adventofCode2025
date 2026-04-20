

class rangeList(GridMap):
    
    # Assume ranges in the index are greater then or equal to 0
    def __init__(self):
        binaryList = []

    # Returns True if the list is empty, otherwise False
    def isEmpty(self):
        if self.getLength() = -1:
            return True
        return False

    # Gets the list length
    def getLength(self):
        return len(binaryList) - 1

    # Gets the ranges at the selected index
    def getRangeAtIndex(self, index):
       if not self._validIndex(self, index):
           return (-1, -1)
       return binaryList[index]

    # Gets the max Range at the selected index
    def getMaxAtIndex(self, index):
        selRange = self.getRangeAtIndex(index)
        
        return selRange[1]

    # Gets the min Range at the selected index
    def getMinAtIndex(self, index):
        selRange = self.getRangeAtIndex(index)
        
        return selRange[0]


    # If new range is valid then will add to list.
    # Will merge ranges that overlap with the new range
    def addRange(self, newRange):
        
        endIndex = self.getLength()
        startIndex = 0

        if not self._validRange(newRange):
            return False

        # TODO Add Binary list search here

        


    # Checks that the passed index is valid within the list of ranges
    def _validIndex(self, index):
        
        if self.isEmpty():
            return False
        if self.getLength() < index:
            return False
        if index < 0:
            return False

    # Return True if the range is valid, else False
    def _validRange(self, inRange):

        minRange = inRange[0]
        maxRange = inRange[1]


        # Checks that the range is int
        if not isinstance(minRange, int):
            return False
        
        if not isinstance(maxRange, int):
            return False

        if minRange < 0:
            return False

        if minRange > maxRange:
            return False

        return True


    # Method to insert a new range at an index
    # Returns True if able to insert at the index, otherwise False
    def _insertRange(self, insertIndex, newRange):

        # Checks that range is valid
        if not self._validRange(newRange):
            return False

        # Checks that the index is valid
        if not self._validIndex(insertIndex):
            return False

        binaryList.insert(insertIndex, newRange)
        return True


    # Method to pop range at an index
    # Returns True if able to pop at the index, otherwise False
    def _popRange(self, popIndex):

        # Checks that index is valid
        if not self._validIndex(popIndex):
            return False

        binaryList.pop(popIndex)
        return True





