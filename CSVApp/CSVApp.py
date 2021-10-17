import tkinter as tk
from tkinter import *
import math
from tkinter.filedialog import askopenfilename
from CommandLineInterface import CommandLineInterface
 
filepath = ""

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=YES)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        if self._frame is not None:
            self._frame.destroy()
        if frame_class == None:
            self.master.destroy()
            quit()
        new_frame = frame_class(self)
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=YES)
        self.create_widgets()
        self.configure(bg="#003F91")
       

    def create_widgets(self):
        #Title Text
        self.titleLabel = tk.Label(self, text="CSVapp", fg="white", bg="#003F91", font=("Arial", 30) )
        self.titleLabel.pack(side=TOP, expand=YES)

        #Select File Button
        self.fileSelect = tk.Button(self, fg="black", height = 5, width = 30)
        self.fileSelect["text"] = "Select File"
        self.fileSelect["command"] = self.openFile
        self.fileSelect.pack(side=TOP, expand=YES)
        self.fileSelect.configure(bg="#003F91")

        #Quit Button
        self.quit = tk.Button(self, text="QUIT", fg="red", command=lambda: self.master.switch_frame(None), height = 5, width = 20)
        self.quit.pack(side=TOP, expand=YES)

    def openFile(self):
        global filepath
        filepath = askopenfilename()
        print(filepath)
        self.master.switch_frame(MainPage)

class MainPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg="#003F91")
        global filepath
        try:
            f = open(filepath, "r+")
        except:
            print("nope")

        filename = str(filepath)
        filename.rsplit('/',1)
        print(filename.rsplit('/',1)[1])
        self.pack(fill=BOTH, expand=YES)

        #Table frame
        self.newFrame = Frame(root, bg='#003F91', width=450, height=50, pady=0.2)
        self.newFrame.pack(side=TOP, expand=YES, fill=BOTH)

        #To interact with file and CSVLibrary
        self.CSVFileAccess = CommandLineInterface(filename.rsplit('/',1)[1], f)

        #Create widgets
        self.create_widgets()
        
        

    def create_widgets(self):
        #Title Text
        self.titleText = tk.Text(self, fg="black")

        #spacer#
        self.spacer5 = Label (self, height=1, width=5, bg='#003F91',  fg='#003F91', highlightbackground='#003F91', state=DISABLED )
        self.spacer5.pack(side=LEFT)

        ##Specify##
        #Button#
        self.specifyButton = Button (self,  text ="Specify Seperator", bg='#003F91', bd=0, command = self.changeSpecify, highlightbackground='#003F91', height=2)
        self.specifyButton.pack(side=LEFT)
        #Entry
        self.specifyEntry = Entry (self, width=1, highlightbackground='#5DA9E9')
        self.specifyEntry.pack(side=LEFT)
        self.specifyEntry.insert( 0, "," )


        #Create list
        lst = self.CSVFileAccess.execute("1")
        print(lst)

        # find total number of rows and 
        # columns in list 
        self.total_rows = len(lst) 
        self.total_columns = len(lst[0]) 

        #Spacer#
        self.spacer3 = Label (self.newFrame, height=1, width=5, bg='#003F91',  fg='#003F91', highlightbackground='#003F91', state=DISABLED)
        self.spacer3.grid(row=0, column=0)

        for i in range(self.total_rows): 
            for j in range(self.total_columns): 
                  
                self.e = Entry(self.newFrame, width=20, fg='blue', 
                               font=('Arial',16,'bold')) 
                self.e.grid(row=i+ 1, column=j + 1)
                self.e.insert(END, lst[i][j]) 

        ##Spacer##
        self.spacer1 = Label (self, height=1, width=10, bg='#003F91',  fg='#003F91', highlightbackground='#003F91', state=DISABLED)
        self.spacer1.pack(side=LEFT)

        ##Get Cell##
        #Get Cell Button
        self.getCellButton = Button (self,  text ="Get Cell", bg='#003F91', bd=0, command = self.getCell, highlightbackground='#003F91', height=2)
        self.getCellButton.pack(side=LEFT)
        #Get cell Entry
        self.getCellEntry = Entry (self, width=5, highlightbackground='#5DA9E9')
        self.getCellEntry.pack(side=LEFT)
        self.getCellEntry.insert( 0, "0, 0" )
        #Get Cell Text
        self.getCellText = Text (self, height=1, width=8)
        self.getCellText.pack(side=LEFT)
        cell = self.getCellEntry.get()
        partitioned_string = cell.partition(',')
        col = partitioned_string[0]
        row = partitioned_string[2] 
        try:
            cellContent = self.CSVFileAccess.execute("3", col, row)
            self.getCellText.delete('1.0', END)
            self.getCellText.insert(END, cellContent)
        except:
            self.getCellText.delete('1.0', END)
            self.getCellText.insert(END, "Invaild Cell")

        #Exit
        self.quit = tk.Button(self, text="Exit File", fg="red", command=self.exitPage, height = 2, width = 5, highlightbackground='#003F91')
        self.quit.pack(side=RIGHT, expand=YES)

        ##Spacer##
        self.spacer2 = Label (self, height=1, width=10, bg='#003F91',  fg='#003F91', highlightbackground='#003F91', state=DISABLED)
        self.spacer2.pack(side=LEFT)

        ##ChangeCell
        self.changeCellButton = Button (self,  text ="Update Cell", bg='#003F91', bd=0, command = self.changeCell, highlightbackground='#003F91', height=2)
        self.changeCellButton.pack(side=LEFT)
        #Get cell Entry
        self.changeCellEntry = Entry (self, width=5, highlightbackground='#5DA9E9')
        self.changeCellEntry.pack(side=LEFT)
        self.changeCellEntry.insert( 0, "0, 0" )
        #Directions
        self.changeCellText = Label (self, text="with", height=1, width=4)
        self.changeCellText.pack(side=LEFT)
        #New datat entry
        self.changeCellDataEntry = Entry (self, width=8, highlightbackground='#5DA9E9')
        self.changeCellDataEntry.pack(side=LEFT)
        self.changeCellDataEntry.insert( 0, "New Data" )


        
    def updateTable(self):
        self.newFrame.destroy()
        self.newFrame = Frame(root, bg='#003F91', width=450, height=50, pady=0.2)
        self.newFrame.pack(side=TOP, expand=YES, fill=BOTH)
        #Create list
        lst = self.CSVFileAccess.execute("1")
        
        #Spacer#
        self.spacer3 = Label (self.newFrame, height=1, width=5, bg='#003F91',  fg='#003F91', highlightbackground='#003F91', state=DISABLED)
        self.spacer3.grid(row=0, column=0)

        # find total number of rows and 
        # columns in list 
        self.total_rows = len(lst) 
        self.total_columns = len(lst[0]) 
        

        for i in range(self.total_rows): 
            for j in range(self.total_columns): 
                self.e = Entry(self.newFrame, width=20, fg='blue', 
                               font=('Arial',16,'bold')) 
                self.e.grid(row=i+ 1, column=j + 1)
                self.e.insert(END, lst[i][j]) 

    def changeSpecify(self):
        specified = self.specifyEntry.get()
        self.CSVFileAccess.execute("2", specified)
        self.updateTable()

    def getCell(self):
        cell = self.getCellEntry.get()
        partitioned_string = cell.partition(',')
        col = partitioned_string[0]
        row = partitioned_string[2] 
        try:
            cellContent = self.CSVFileAccess.execute("3", col, row)
            self.getCellText.delete('1.0', END)
            self.getCellText.insert(END, cellContent)
        except:
            self.getCellText.delete('1.0', END)
            self.getCellText.insert(END, "Invaild Cell")

    def changeCell(self):
        cell = self.getCellEntry.get()
        partitioned_string = cell.partition(',')
        col = partitioned_string[0]
        row = partitioned_string[2] 
        data = self.changeCellDataEntry.get()
        try:
            self.CSVFileAccess.execute("4", col, row, data)
            self.updateTable()
        
        except:
            self.getCellText.delete('1.0', END)
            self.changeCellText.insert(END, "Invaild Cell")

    def exitPage(self):
        self.newFrame.destroy()
        self.master.switch_frame(StartPage)

                
        

root = tk.Tk(className="csvApp")
root.geometry("1000x600")
root.configure(bg="#003F91")
app = Application(master=root)
app.mainloop()

