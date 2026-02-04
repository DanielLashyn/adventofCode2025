from classes.rotation import rotation

class dial:
    def __init__(self, selectStartPostion=50):
        self.setPostion(selectStartPostion)
        self.timesOnZero = 0

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


    def updatePostion(self, rotationValue):
        if not isinstance(rotationValue, rotation):
            print("Error: RotatoinValue is not the correct class!")
            return

        direction = rotationValue.getDirection()
        distance = rotationValue.getDistance()

        # Subtract to the postion
        if direction == 'L':
            total = self.postion - distance
        
        # Adds to the postion
        if direction == 'R':
            total = self.postion + distance

        self.postion = abs(total % 100)
 
        if(self.postion == 0):
            self.timesOnZero += 1

    # Print out the values for the user to see
    def printValues(self):
        print("Postion: " + str(self.postion))
        print("Number of times on 0: " + str(self.timesOnZero))
