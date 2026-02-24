from globalCode.interfaceFileReader import interfaceFileReader as parent


class fileReaderOneLine(parent):

    def __init__(self, delimiter = None):
        super().__init__(delimiter = delimiter)


    def setData(self,filePath="NONE"):
        
        if(filePath == "NONE"):
            return

        self.dataFile = filePath
        # Gets the raw data from the text file
        try:
           with open(filePath, "r") as file:
                rawData = file.readline().rstrip("\n")
                rawData = rawData.split(self.delimiter)
        except FileNotFoundError:
            rawData = "Error: Unable to find file at " + str(filePath)
        self.data = rawData
    
