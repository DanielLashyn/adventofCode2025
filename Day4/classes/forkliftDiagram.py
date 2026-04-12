from globalCode.classGridMap import GridMap

class forkliftDiagram(GridMap):

    def __init__(self, gridData):
        super().__init__(gridData = gridData)

    def getAccessableRolls(self, replace = False):
        accessableRolls = 0
        isRoll = 0
        counter = 0
        for y in range(0, self.row):

            for x in range(0, self.column):
                isRoll = self.countCharInSection(centerCords = (x,y), 
                    wantedChar = '@', 
                    distanceFromCenter = 0)
                if isRoll >= 1:
                    counter = self.countCharInSection(centerCords = (x,y), 
                        wantedChar = '@', 
                        distanceFromCenter = 1)
                
                    if counter <= 4:
                        accessableRolls += 1

                        if replace:
                           self.updateMapValue((x,y), "x")

                isRoll = 0
                counter = 0
                
        return accessableRolls



