from .equationList import equationList

class advanceEquationList(equationList):

    def __init__(self):
        super().__init__()


    # advance version of init Data
    def initData(self, data):

        dataLength = len(data)
        columnLength = self.getDataLength(data)

        for column in range (columnLength - 1, -1, -1):
            equationStr = ""
            for row in range (0, dataLength - 1):
                temp = data[row]
                equationStr = equationStr + str(temp[column])
            print(equationStr)

    def getDataLength(self, data):

        maxValue = 0
        for i in range(0, len(data) - 1):
            maxValue = max(maxValue, len(data[1]))

        return maxValue

