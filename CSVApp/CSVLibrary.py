from CommandLineInterface import CommandLineInterface

#----------------------------------------------------
if __name__=="__main__":
    selection = "NULL"

    print("~Welcome to CSVLibrary~")
    
    #Main loop for command selection
    openedFile = False

    fileName = input("\nEnter in the filename (with extension): ")

    while openedFile == False:
        try: 
            f = open(fileName, "r+")
            openedFile = True
            commanndInterface = CommandLineInterface(fileName, f)
            while(selection != "6"):
                print("\nSelect an operation by number... (ex. \'1\', \'2\', ect)")
                commanndInterface.printCommands()
                selection = input("\nSelection: ")
                commanndInterface.execute(selection)
            selection = "0"
            openedFile = False

            goAgain = input("Would you like to open another file? (Y or N): ")

            if(goAgain.upper() != 'Y'):
                print("\n~Program terminated~\n")
                break
            else:
                fileName = input("\nEnter in the filename (with extension): ")
        except:
           print("\nError: Unable to open file.\n")
           fileName = input("Enter in the file name (with extension): ")
        
