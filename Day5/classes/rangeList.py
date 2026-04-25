class rangeList():
    
    # Assume ranges in the index are greater then or equal to 0
    def __init__(self):
        self.binaryList = []
    

    # Returns True if the list is empty, otherwise False
    def isEmpty(self):
        if self.getLength() == -1:
            return True
        return False

    # Gets the list length
    def getLength(self):
        return len(self.binaryList) - 1

    # Gets the ranges at the selected index
    def getRangeAtIndex(self, index):
       if not self._validIndex(index):
           return (-1, -1)
       
       return self.binaryList[index]

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
       
        newRange = self.convertStringToRange(newRange)
        endIndex = self.getLength()
        startIndex = 0

        if not self._validRange(newRange):
            return False

        if endIndex == -1:
            self.binaryList.append(newRange)
            return True
        
        
        # TODO Add Binary list search here
        while startIndex <= endIndex:
            mid = (endIndex + startIndex) // 2

            if self.getMaxAtIndex(mid) < newRange[0]:
                print(str(self.getMaxAtIndex(mid)) + " < " + str(newRange[0]))
                startIndex = mid + 1
            else:
                print(str(self.getMaxAtIndex(mid)) + " > " + str(newRange[0]))
                
                endIndex = mid - 1
        
        print(startIndex)
        self._insertRange(startIndex, newRange)


    # Checks that the passed index is valid within the list of ranges
    def _validIndex(self, index):
            
        # Special condition for empty list
        if self.isEmpty():
            return False

        # checks that the index is not greater then the length
        if self.getLength() < index:
            return False

        # Checks that index is not less then 0
        if index < 0:
            return False
        
        return True
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
        #if not self._validIndex(insertIndex):
            #return False
        
        self.binaryList.insert(insertIndex, newRange)
        return True


    # Method to pop range at an index
    # Returns True if able to pop at the index, otherwise False
    def _popRange(self, popIndex):

        # Checks that index is valid
        if not self._validIndex(popIndex):
            return False

        self.binaryList.pop(popIndex)
        return True

    def display(self):
        print(self.binaryList)

    def convertStringToRange(self, strRange):
        
        if not isinstance(strRange, str):
            return None

        splitRange = strRange.split('-')
        return (int(splitRange[0]), int(splitRange[1]))


