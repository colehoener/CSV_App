from prettytable import *
from collections import Counter 

class CSVFileReader():
    def __init__(self, fileName, file):
        self.fileName = fileName
        self.file = file
        self.file.seek(0)
        self.fileContents = file.read()
        self.seperator = ','
        self.prettyTable = PrettyTable() #rows
        self.basicTable = []
        self.createTable()

    def printTable(self):
        print(self.prettyTable)

    def getTable(self):
        return self.basicTable

    def setFile(self, file):
        self.file = file
        self.file.seek(0)
        self.fileContents = file.read()
    
    def createTable(self):
        self.basicTable = []
        seperator = self.seperator
        splitItems = self.fileContents.split('\n')
        flag = False
        totalColumns = 0

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

        self.prettyTable.clear()

        for i in self.basicTable:
            if (flag == False):
                self.prettyTable.field_names = (i)
                flag = True
            else:
                self.prettyTable.add_row(i)

    def specifySeperator(self, newSeperator):
        self.seperator = newSeperator
        self.basicTable = []
        self.createTable()
       
    
    def retrieveCell(self, row, column):
        self.createTable()
        try:
            return (self.basicTable[int(row)][int(column)])
        except:
            return ("Invalid cell.")
