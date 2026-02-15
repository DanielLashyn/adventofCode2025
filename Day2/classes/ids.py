class ids:
    def __init__(self, idRanges):
        self.setStartid(idRanges)

    def setStartid(self, passID):

        if isinstance(passID, str) and passID.isdigit():
            self.startID = int(passID)

        elif isinstance(passID, int):
            self.startID = passID

        else:
            print("Error: Not valid start id")
            self.startID = 0



    def display(self):
        print("Starting ID: " + str(self.startID))

