# This is the parentClass for all the DataLoader classes to use
class interfaceFileReader():
    
    def __init__(self):
        self.dataFile = ""
        self.data = []
        pass

    def setData(self):
        pass

    def getData(self):
        return self.data

    def displayData(self):
        print("Data From: " + str(self.dataFile))
        print("Data: \n" + str(self.data))
