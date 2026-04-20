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

    """
        Description: Counts the number of times a character appers in a section of the grid
        Inputs:
            - centerCords: Tuple (x,y) cords of where the center of the section is
            - wantedChar: Character that is beingCounted in the section
            - distanceFromCenter: How far from the center to make the section 
        Output:
            - returns the number of times the character appeared

    """
    def countCharInSection(self, centerCords = (0,0), 
            wantedChar = ',', 
            distanceFromCenter = 1):

        if not isinstance(centerCords,tuple) or len(centerCords) != 2:
            print("GridMap Error: Not valid cords!")
            return
        
        xCord = centerCords[0]
        yCord = centerCords[1]
        
        if not isinstance(xCord, int) or xCord < 0 or xCord > self.column:
            print("GridMap Error: Not Valid X cord!")
            return

        if not isinstance(yCord, int) or yCord < 0 or yCord > self.row:
            print("GridMap Error: Not Valid y cord!")
            return

        if not isinstance(wantedChar, str):
            print("GridMap Error: Lookup value must be string!")
            return

        if distanceFromCenter < 0:
            print("GridMap Error: Distance Must be greater then 0!")
            return 0

        counter = 0

        # Looks through all the rows and columns in the section
        for rowLocation in range (yCord - distanceFromCenter, yCord + distanceFromCenter + 1):
            
            # Checks that the row location is not outside
            if rowLocation >= self.row:
                break

            if rowLocation < 0:
                rowLocation = 0
                continue

            rowData = self.gridData[rowLocation]
            
            # Looks through all the columns for that row
            for columnLocation in range(xCord - distanceFromCenter, xCord + distanceFromCenter + 1):
                
                # Checks that the column location is not outside
                if columnLocation >= self.column:
                    break
                
                if columnLocation < 0:
                    columnLocation
                    continue

                data = rowData[columnLocation]
                               
               
                # If data matchs the wanted char then added one
                if str(data) == wantedChar:
                    counter += 1

        return counter

    def display(self):
        
        if not self.gridData:
            print("There is no Grid Map to display!")
            return

        self._displayGridMap(self.gridData)

    def _displayGridMap(self, gridData, rowOffSet = 0, columnOffSet = 0):
        # Prints the column header
        columnHeaderString = "  "
        for columnHead in range(columnOffSet, len(gridData[0]) + columnOffSet):
            columnHeaderString += " " + str(columnHead)
        print(columnHeaderString)
        print("  "+ (len(gridData[0]) * " _"))

        for rowCount, rowData in enumerate(gridData):
            print(str(rowCount + rowOffSet) + "|" , end = "")
            
            for data in rowData:
                print(" "+ str(data), end = "")

            print()

    def displaySection(self, rowRange, columnRange):
        
        # Checks that the ranges are valid
        if not self._isValidRange(rowRange, self.row):
           #not self._isValidRange(columnRange, self.column):
            print("Unable to Display!")
            return 

        # Gets the Data
        gridData = [row[columnRange[0]:columnRange[1] + 1] for row in 
                self.gridData[rowRange[0]:rowRange[1] + 1]]
        
        # Displays the grid
        self._displayGridMap(gridData, 
                rowOffSet = rowRange[0], 
                columnOffSet = columnRange[0])

    def updateMapValue(self, inRange, value):
       
        # Do values check here

 
        xCord = inRange[0]
        yCord = inRange[1]
        if not isinstance(xCord, int) or xCord < 0 or xCord > self.column:
            print("GridMap Error: Not Valid X cord!")
            return

        if not isinstance(yCord, int) or yCord < 0 or yCord > self.row:
            print("GridMap Error: Not Valid y cord!")
            return       

        self.gridData[yCord][xCord] = value

        

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

        if inRange[0] > inRange[1]:
            print("GridMap Error: is not a valid range")
            return False

        return True


