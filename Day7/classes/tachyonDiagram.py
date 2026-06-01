class tachyonDiagram():


    def __init__(self):
        self.diagram = [[]]
        self.locationS = (0,-1) # (x,y)
        self.allSplitters = [] # [(x1,y1), (x2,y2)....(xn, yn)]
        self.splittersUsed = 0

    def getHeight(self):
        return len(self.diagram)

    def getLength(self):
        return len(self.diagram[0])

    def countAllSplitters(self):
        return len(self.allSplitters)

    def validStartingLocation(self):
        if self.locationS == (0,-1):
            return False
        return True
    def getSplittersUsed(self):
        return self.splittersUsed

    def setDiagram(self, inDiagram):
        tempDiagram = []
        rowIndex = 0
        colIndex = 0
        splitters = []

        # Finds the location of S in the first Row
        Slocation = inDiagram[0].find('S')

        # checks that the Slocation is valid
        if Slocation == -1:
            print("Error: Given Diagram doesn't have a valid starting location!")
            return False
       
        # Gets the length of the first row, to match against other rows 
        rowLength = len(inDiagram[0])

        # Formats the inDiagram to be a 2d List
        for row in inDiagram:
            
            tempRow = []

            if len(row) != rowLength:
                print("Error: Given Diagram doesn't have equal rows!")
                return False

            # converts each row to a list
            for item in row:
                tempRow.append(str(item))
                
                # If current selection is a splitter then adds it to the list
                if str(item) == '^':
                    splitters.append((colIndex, rowIndex))

                colIndex += 1

            tempDiagram.append(tempRow)

            rowIndex += 1
            colIndex = 0
        # Sets the global variables
        self.diagram = tempDiagram
        self.locationS = (Slocation,0)
        self.allSplitters = splitters
        return True

    def setBeams(self):
        splittersHit = 0

        if not self.validStartingLocation():
            return False

        beamLocations = {self.locationS[0]}
        for row in self.diagram:
            beamsToRemove = []

            for beam in beamLocations:

                if (row[beam] == '.'):
                    row[beam] = '|'
                elif row[beam] == '^':
                    beamsToRemove.append(beam)
                    splittersHit += 1

            for beam in beamsToRemove:
                beamLocations.discard(beam)
                beamLocations.update([beam - 1, beam + 1])
        
        self.splittersUsed = splittersHit

    def display(self):

        for row in self.diagram:
            for item in row:
                print(item, end="")
            print()
        print("Total Splitters: " + str(self.countAllSplitters()))
        print("Total Splitters used: " + str(self.splittersUsed))
        print("Starting Location is: " + str(self.locationS))
