def equation():

    def __init__(self):
        self.numbers = []
        self.operator = ""

    # Gets the number of numbers in the equation
    def getLength(self):
        return len(numbers)

    # Gets the number at a selected index
    def getNumAtIndex(self, index):

        # Checks that there are numbers in the equation
        if self.isEmpty():
            return -1
        # Checks that the index given was valid
        if not self.validIndex():
            return -1

        # Returns the number at the index
        return self.numbers[index]

    # appended a new number to the end of the equation
    def append(self, value):

        if not isinstance(value, int):
            return False

        self.numbers.append(value)
        return True

    # Removes the end number from the equation
    def pop(self):

        # Checks that there is a number to pop
        if self.isEmpty():
            return False

        self.numbers.pop()

    # Returns true if there are no numbers in the equation
    # Otherwise false
    def isEmpty(self):

        if self.getLength() == 0:
            return True

        return False
    
    # Sets the operator value 
    def setOperator(self, inputOperator):

        if not isinstance(inputOperator, str):
            return False

        # Sets the operator if it's a valid operation
        if inputOperator == "*":
            self.operator = "*"
        elif inputOperator == "+":
            self.operator = "+"
        else:
            return False

        return True

    def getOperator(self):
        return self.operator

    # Gets the result of the equation
    def getResult(self):

        # If equation is empty then return 0
        if self.isEmpty():
            return 0

        # Checks that the operator value was set
        if self.getOperator() == "":
            return 0

        if self.getOperator() == "*":
            result = 1
        else:
            result = 0


        for term in self.numbers:

            if self.getOperator() == "*":
                result = result * term
            elif self.getOperator() == "+":
                result = result + term
            else:
                break

        return result

    def display(self):
        print(self.numbers)
        print(self.getOperator())
        print(self.getResult())
