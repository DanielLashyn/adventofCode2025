class rotation:
    def __init__(self, rotationCombo):
       
        self.setDirection(rotationCombo)
        self.distance = 9

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


    def printValues(self):
        print("Direction: " + self.direction)
        print("Distance: " + str(self.distance))

