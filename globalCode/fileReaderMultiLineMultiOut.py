from globalCode.interfaceFileReader import interfaceFileReader as parent


class fileReaderMultiLineMultiOut(parent):

    def __init__(self):
        super().__init__()


    def setData(self,filePath="NONE", delimiter = ','):
        
        rawData = []
        if(filePath == "NONE"):
            return
        try:
            with open(filePath, "r") as file:
                for line in file:
                    row = line.strip()
                    row = list(row)
                    rawData.append(row)
        except FileNotFoundError:
            rawData = "Error: Unable to find file at " + str(filePath)
        
        self.data = rawData

    def displayData(self):
        
        if not self.data:
            print("No data has been read!")
            return

        for row in self.data:
            print(row)
                    
