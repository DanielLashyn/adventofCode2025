from .equationList import equationList
from .equation import equation

class advanceEquationList(equationList):

    def __init__(self):
        super().__init__()


    # advance version of init Data
    def initData(self, data):

        dataLength = len(data)
        columnLength = self.getDataLength(data)

        curEquation = equation()
        # Loops through all the columns, from right to left
        for column in range (columnLength - 1, -1, -1):
            equationStr = ""
            for row in range (0, dataLength - 1):
                temp = data[row]
                equationStr = equationStr + str(temp[column])

            # Removes the whitespace
            equationStr = equationStr.strip()

            # Creates a new equation if the current line is empty
            # Otherwise add numbers to current equation
            if equationStr == "":
                self.equations.append(curEquation)
                curEquation = equation()
            else:
                curEquation.append(equationStr)
        
        self.equations.append(curEquation)

        # Sets the operator for the equations
        operators = data[-1].split()
        operatorLength = len(operators)

        for operator in operators:
            operatorLength -= 1
            self.equations[operatorLength].setOperator(operator)
        
    def getDataLength(self, data):

        maxValue = 0
        for i in range(0, len(data) - 1):
            maxValue = max(maxValue, len(data[1]))

        return maxValue

