class GridMap:
    def __init__(self, gridData):
        self.setGridMap(gridData)

    def setGridMap(self, gridData):
        
        if not self._isValidGridMap(gridData):
            return False
        
        self.GridData = gridData
        self.row = len(gridData[0])
        self.column = len(gridData)
    
    def _isValidGridMap(self, gridData):
       
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



           
