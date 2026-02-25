class GridMap:
    def __init__(self, gridData):
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
            print("There is no Grid Mao to display!")
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





           
