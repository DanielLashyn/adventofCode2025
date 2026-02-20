from globalCode.interfaceFileReader import interfaceFileReader as parent


class fileReaderOneLine(parent):

    def __init__(self):
        super().__init__()


    def setData(self,filePath="NONE", delimiter = ','):
        
        if(filePath == "NONE"):
            return

        self.dataFile = filePath
        # Gets the raw data from the text file
        with open(filePath, "r") as file:
            rawData = file.readline().rstrip("\n")
            rawData = rawData.split(delimiter)
        self.data = rawData
    
