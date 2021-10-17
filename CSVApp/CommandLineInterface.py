from CSVFileReader import CSVFileReader
from CSVEditor import CSVEditor

class CommandLineInterface():
    def __init__(self, fileName, file):
        self.commandList = ["1. View CSVFile", "2. Sepcify seperator", "3. Retrieve cell", "4. Replace cell", "5. Change seperator", "6. Exit file and save changes"]
        self.fileName = fileName
        self.file = file
        self.viewFile = CSVFileReader(self.fileName, self.file)
        self.editFile = CSVEditor(self.fileName, self.file)

    def printCommands(self):
        for i in self.commandList:
            print(i)

    def execute(self, command, arg1=None, arg2=None, arg3=None):
        if(command == "1"):
            return self.viewFile.getTable()
        elif(command == "2"):
            self.viewFile.specifySeperator(arg1)
            self.editFile.specifySeperator(arg1)
        elif(command == "3"):
            col = arg1
            row = arg2
            return self.viewFile.retrieveCell(row, col)
        elif(command == "4"):
            col = arg1
            row = arg2
            newData = arg3
            self.editFile.replaceCell(row, col, newData)
            file = open(self.fileName, "r+")
            self.editFile.setFile(file)
            self.viewFile.setFile(file)
            self.editFile.createTable()
            self.viewFile.createTable()
            
        elif(command == "5"):
            newSeperator = input("Enter the new seperator: ")
            self.editFile.replaceSeperator(newSeperator)
            self.editFile.createTable()
            self.viewFile.createTable()
        elif(command == "6"):
            print("\n~File exited~\n")
        else:
            print("Invalid operation selection. Try again.")
        