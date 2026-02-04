class rotation:
    def __init__(self, rotationCombo):
       
        self.setDirection(rotationCombo)
        self.setDistance(rotationCombo)

    # Set the direction that the dial needs to be spinned
    # Input: 
    #       - rotationCombo: String object that contains the letters L or R.
    # Output: If no letter is found the direction is set to ""
    def setDirection(self, rotationCombo):
       
        # Checks that the object is  string
        if not isinstance(rotationCombo, str):
            self.direction = ''
            return
        
        for char in rotationCombo:
            if char == 'L' or char == 'R':
                self.direction = char
                return

        # If it gets to this point then no letter was found

        self.direction = ''

    # Set the distance that the dial needs to be moved
    # Input:
    #       - rotation Combo: Can either be a string with numbers in it or integer/float
    # Output: If the input is valid then sets the distance to be that value, otherwise 0
    def setDistance(self, rotationCombo):
        
        if isinstance(rotationCombo, str):
            self.distance = int(''.join(char for char in rotationCombo if char.isdigit()))
            return

        if isinstance(rotationCombo, int):
            self.distance = rotationCombo
            return

        if isinstance(rotationCombo, float):
            self.distance = int(rotationCombo)
            return

        # Gets here means the input wasn't valid
            self.distance = 0



    def getDirection(self):
        return self.direction

    def getDistance(self):
        return self.distance


    def printValues(self):
        print("Direction: " + self.direction)
        print("Distance: " + str(self.distance))

