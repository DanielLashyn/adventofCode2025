from globalCode.interfaceFileReader import interfaceFileReader as parent


class fileReaderMultiLine(parent):

    def __init__(self):
        super().__init__()


    def setData(self,filePath="NONE"):
        
        if(filePath == "NONE"):
            return
        try:
            with open(filePath, "r") as file:
                rawData = file.read().splitlines()
        except FileNotFoundError:
            rawData = "Error: Unable to find file at " + str(filePath)
        
        self.data = rawData

