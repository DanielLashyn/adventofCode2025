class GridMap:
    def __init__(self, gridData):
        
        self.gridData = []
        self.row = 0
        self.column = 0

        self.setGridData(gridData)

    def setGridData(self, gridData):
        
        if not self._isValidGridData(gridData):
            print("GridMap Error: Unable to set gridData")
            return False
        
        self.gridData = gridData
        self.row = len(gridData[0])
        self.column = len(gridData)
    
    def _isValidGridData(self, gridData):
       
        # Checks that gridData has data        
        if not gridData:
            print("GridMap Error: gridData is empty!")
            return False

        # Checks that gridData is at least a 2d list
        if not isinstance(gridData, list) or not isinstance(gridData[0], list):
            print("GridMap Error: gridData is not a 2D list!")
            return False

        rowLength = len(gridData[0])

        # Checks that gridData is a valid map
        for row in gridData:
                        
            if len(row) != rowLength:
                print("GridMap Error: gridData is valid 2D list")
                return False

        return True

    def display(self):
        
        if not self.gridData:
            print("There is no Grid Map to display!")
            return

        # Prints the column header
        columnHeaderString = "  "
        for columnHead in range(0, self.column):
            columnHeaderString += " " + str(columnHead)
        print(columnHeaderString)
        print("  "+ (self.column * " _"))

        for rowCount, rowData in enumerate(self.gridData):
            print(str(rowCount) + "|" , end = "")
            
            for data in rowData:
                print(" "+ str(data), end = "")

            print()

    def displaySection(self, rowRange, columnRange):
        
        # Checks that the ranges are valid
        if not self._isValidRange(rowRange, self.row):
           #not self._isValidRange(columnRange, self.column):
            print("Unable to Display!")
            return

        data = self.gridData[columnRange[0]:columnRange[1]][rowRange[0]:rowRange[1]])
        
    def _isValidRange(self, inRange, maxRange):
        
        if not isinstance(inRange, tuple):
            print("GridMap Error: Range is not a tuple!")
            return False

        if len(inRange) != 2:
            print("GridMap Error: Range is not exactly 2 values!")
            return False

        if not all(isinstance(i, int) for i in inRange):
            print("GridMap Error: Range is not integer")
            return False

        if not all( (i >= 0 and i < maxRange) for i in inRange):
            print("GridMap Error: is not a valid range")
            return False

        #if not all(inRange[0] > inRange[1]):
            #print("GridMap Error: is not a valid range")
            #return False


        return True



