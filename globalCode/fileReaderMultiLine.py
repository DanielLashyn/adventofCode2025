from globalCode.interfaceFileReader import interfaceFileReader as parent


class fileReaderMultiLine(parent):

    def __init__(self):
        super().__init__()


    def setData(self,filePath="NONE", delimiter = ','):
        
        if(filePath == "NONE"):
            return

        with open(filePath, "r") as file:
             rawData = file.read().splitlines()
        self.data = rawData

