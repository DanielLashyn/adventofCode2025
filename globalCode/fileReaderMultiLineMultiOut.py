from globalCode.interfaceFileReader import interfaceFileReader as parent


class fileReaderMultiLineMultiOut(parent):

    def __init__(self, delimiter = None):
        super().__init__(delimiter = delimiter)


    def setData(self,filePath="NONE"):
        rawData = []
        if(filePath == "NONE"):
            return
        try:
            with open(filePath, "r") as file:
                for line in file:
                    row = line.strip()
                    
                    if self.delimiter == None:
                        row = list(row)
                    else:     
                        row = row.split(self.delimiter) 

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
                    
