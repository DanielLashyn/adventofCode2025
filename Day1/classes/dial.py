class dial:
    def __init__(self, selectStartPostion=50):
        self.setPostion(selectStartPostion)


    # Sets the starting postion of the dial
    # Input:
    #   -setStartPostion: Integer value that is within range of the dial
    # Output: startPostion set to setStartPostion if input is valid, otherwise -1
    def setPostion(self, selectStartPostion):
        # Checks that input is integer
        if not isinstance(selectStartPostion,int):
            self.postion = -1
            print("Error: Not valid input type for Dial")
            return

        # Checks that input is within range
        if selectStartPostion <= -1 or selectStartPostion >= 100:
            self.postion = -1
            print("Error: Starting postion for dail is out of range")
            return
        self.postion = selectStartPostion


    def printValues(self):
        print("Postion: " + str(self.postion))
