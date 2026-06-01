class tachyonDiagram():


    def __init__(self):
        self.diagram = [[]]
        self.locationS = (0,-1) # (x,y)


    def getHeight(self):
        return len(self.diagram)

    def getLength(self):
        return len(self.diagram[0])

    def setDiagram(self, inDiagram):
        tempDiagram = []

        # Finds the location of S in the first Row
        Slocation = inDiagram[0].find('S')

        # checks that the Slocation is valid
        if Slocation == -1:
            print("Error: Given Diagram doesn't have a valid starting location!")
            return 1
       
        # Gets the length of the first row, to match against other rows 
        rowLength = len(inDiagram[0])
       
        # Formats the inDiagram to be a 2d List
        for row in inDiagram:
            
            tempRow = []

            if len(row) != rowLength:
                print("Error: Given Diagram doesn't have equal rows!")
                return 2

            # converts each row to a list
            for item in row:
                tempRow.append(str(item))

            tempDiagram.append(tempRow)

        # Sets the global variables
        self.diagram = tempDiagram
        self.locationS = (Slocation,0)


    def display(self):

        for row in self.diagram:
            for item in row:
                print(item, end="")

            print()
        print("Starting Location is: " + str(self.locationS))
