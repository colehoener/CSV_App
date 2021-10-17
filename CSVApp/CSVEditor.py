class CSVEditor():
    def __init__(self, fileName, file):
        self.fileName = fileName
        self.file = file
        self.file.seek(0)
        self.fileContents = file.read()
        self.seperator = ','
        self.basicTable = []
        self.createTable()
    
    def setFile(self, file):
        self.file = file
        self.file.seek(0)
        self.fileContents = file.read()

    def createTable(self):
        seperator = self.seperator
        splitItems = self.fileContents.split('\n')
        flag = False
        totalColumns = 0
        self.basicTable = []

        for j in splitItems:
            tempSplitRow = j.split(seperator)
            if len(tempSplitRow) > totalColumns:
                    totalColumns = len(tempSplitRow)

        for i in splitItems:
            tempRow = []
            for k in range(0, totalColumns):
                splitRow = i.split(seperator)
                if (k < len(splitRow)):
                    tempRow.append(splitRow[k])
                else:
                    tempRow.append(" ")
                
            self.basicTable.append(tempRow)

    def specifySeperator(self, newSeperator):
        self.seperator = newSeperator
        self.basicTable = []
        self.createTable()

    def replaceSeperator(self, newSeperator):
        if (len(newSeperator) == 1):
            self.fileContents = self.fileContents.replace(self.seperator, newSeperator)
            self.file.seek(0)
            self.file.truncate(0)
            self.file.write(self.fileContents)
        else:
            print("Invalid entry for new seperator.")

    
    def replaceCell(self, row, column, newData):
        self.basicTable[int(row)][int(column)] = newData
        self.file.seek(0)
        self.file.truncate(0)
        for idx1, i in enumerate(self.basicTable):
            for idx, j in enumerate(i):
                self.file.write(j)
                if(idx < len(i) - 1):
                    self.file.write(self.seperator)
            if(idx1 < len(self.basicTable) - 1):
                self.file.write('\n')
        self.file.close()