from .equation import equation

class equationList():

    def __init__(self):
        self.equations = []

    # Gets the number of equation
    def getLength(self):
        return len(self.equations)

    # Gets the equation at a selected index
    def getEquationAtIndex(self, index):

        # Checks that there are numbers in the equation
        if self.isEmpty():
            return -1
        # Checks that the index given was valid
        if not self._validIndex(index):
            return -1

        # Returns the number at the index
        return self.equations[index]
    
    # Method to check that the given index is valid
    def _validIndex(self, index):
            
        # Special condition for empty list
        if self.isEmpty():
            return False

        # checks that the index is not greater then the length
        if self.getLength() < index:
            return False

        # Checks that index is not less then 0
        if index < 0:
            return False
        
        return True

    # appended a new equation to the list
    def appendEquation(self, value):

        if not isinstance(value, equation):
            return False

        self.equations.append(value)
        return True

    # Removes the end equation
    def pop(self):

        # Checks that there is a equation to pop
        if self.isEmpty():
            return False

        self.equation.pop()

    # Returns true if there are no equations
    # Otherwise false
    def isEmpty(self):

        if self.getLength() == 0:
            return True

        return False


    def initData(self, data):

        currentLine = 0
        
        for line in data:
            currentLine += 1
            count = -1

            line = line.split()
    
            for item in line:
                count += 1
                if currentLine == 1:
                    temp = equation()
                    temp.append(item)
                    self.equations.append(temp)
                else:
                    self.equations[count].append(item)

        
    # Gets the result of all the equations
    def getResult(self):

        # If there are no equations return 0
        if self.isEmpty():
            return 0

        result = 0
        for equation in self.equations:
            result = result + equation.getResult()

        return result

    def display(self):
        
        for equation in self.equations:
            equation.display()
