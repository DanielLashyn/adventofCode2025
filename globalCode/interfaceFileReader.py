# This is the parentClass for all the DataLoader classes to use
class interfaceFileReader():
    
    def __init__(self):
        print("Parent")
        self.data = []
        pass

    def setData(self):
        pass

    def getData(self):
        return self.data
