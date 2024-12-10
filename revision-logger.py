from tkinter import *
import os

def readLogged():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'subjects.txt')

    try:
        f = open(file_path, 'r')
        f.close()

    except Exception as e:
        print(f"A <{e}> exception occured!")
        print(f"No such file <{file_path}> exists in the directory!\nCreating file...")

        # create file if not present
        f = open(file_path, 'x')
        f.close()

        print(f"New file <{file_path}> created in the directory!\nBeginning data read...")

    with open(file_path, 'r') as f:
        lines = f.readlines()
        logged = {}

        for entry in lines:
            data = entry.split(",")
            logged[data[0]] = [int(data[1]), int(data[2])]
        
        f.close()
    return logged

def writeLogged(logged):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'subjects.txt')

    with open(file_path, 'w') as f:
        for entry in logged:
            f.write(f"{entry},{logged[entry][0]},{logged[entry][1]}\n")
        
        f.close()

def setupGUI(logged):
    root = Tk()
    root.title("Revision Logger")
    root.geometry('540x350')

    PADX = (5,0)
    PADY = (2.5,0)
    
    tableItems = {}

    def addToTable(subjectName):
        global rowNum

        subjectTime = logged[subjectName][0]
        subjectGoal = logged[subjectName][1]

        progress = 0
        try:
            progress = int(100*subjectTime/subjectGoal)
        except ZeroDivisionError:
            print(f"<{subjectName}> has no goal time set!")

        tableItems[subjectName] = [Label(root, text=subjectName),
                                   Label(root, text=subjectTime),
                                   Label(root, text=subjectGoal),
                                   Label(root, text=f"{progress}%")
        ]

        tableItems[subjectName][0].grid(row=rowNum, column=5, columnspan=4, padx=PADX, pady=PADY)
        tableItems[subjectName][1].grid(row=rowNum, column=9, columnspan=2, padx=PADX, pady=PADY)
        tableItems[subjectName][2].grid(row=rowNum, column=11, columnspan=2, padx=PADX, pady=PADY)
        tableItems[subjectName][3].grid(row=rowNum, column=13, columnspan=2, padx=PADX, pady=PADY)

        print(f"The row number of the next subject is <{rowNum+1}>")
        rowNum += 1

    def updateTable(subjectName):
        subjectTime = logged[subjectName][0]
        subjectGoal = logged[subjectName][1]

        progress = 0
        try:
            progress = int(100*subjectTime/subjectGoal)
        except ZeroDivisionError:
            print(f"<{subjectName}> has no goal time set!")

        tableItems[subjectName][1].config(text=subjectTime)
        tableItems[subjectName][2].config(text=subjectGoal)
        tableItems[subjectName][3].config(text=f"{progress}%")


    for subject in logged:
        addToTable(subject)
    
    #-----# section headers
    addHeader = Label(root, text="Add Subject").grid(                               row=0,   column=0,  columnspan=5, padx=PADX, pady=PADY)
    goalHeader = Label(root, text="Set Goal").grid(                                 row=5,   column=0,  columnspan=5, padx=PADX, pady=PADY)
    logHeader = Label(root, text="Log Progress").grid(                              row=10,  column=0,  columnspan=5, padx=PADX, pady=PADY)
    subjectTableHeader = Label(root, text="Subject Name").grid(                     row=0,   column=5,  columnspan=4, padx=PADX, pady=PADY)
    completedTableHeader = Label(root, text="Time Completed").grid(                 row=0,   column=9,  columnspan=2, padx=PADX, pady=PADY)
    goalTableHeader = Label(root, text="Time Goal").grid(                        row=0,   column=11, columnspan=2, padx=PADX, pady=PADY)
    progressTableHeader = Label(root, text="Progress").grid(                        row=0,   column=13, columnspan=2, padx=PADX, pady=PADY)

    #-----# adding subjects
    addNameLabel = Label(root, text="Name:").grid(                                  row=1,   column=0,  columnspan=2, padx=PADX, pady=PADY, sticky='w')
    addNameEntry = Entry(root, width=24)
    addNameEntry.grid(                                                              row=1,   column=2,  columnspan=3, padx=PADX, pady=PADY, sticky='w')

    addDivider = Label(root, text="------------------------------------").grid(     row=4,   column=0,  columnspan=5, padx=PADX, pady=PADY)

    #-----# setting goals
    goalNameLabel = Label(root, text="Name:").grid(                                 row=6,   column=0,  columnspan=2, padx=PADX, pady=PADY, sticky='w')
    goalNameEntry = Entry(root, width=24)
    goalNameEntry.grid(                                                             row=6,   column=2,  columnspan=3, padx=PADX, pady=PADY, sticky='w')

    goalTimePrefix = Label(root, text="Time:").grid(                                row=7,   column=0,  columnspan=2, padx=PADX, pady=PADY, sticky='w')
    goalTimeEntry = Entry(root, width=5)
    goalTimeEntry.grid(                                                             row=7,   column=2,  columnspan=1, padx=PADX, pady=PADY, sticky='w')
    goalTimeSuffix = Label(root, text="minutes").grid(                              row=7,   column=3,  columnspan=2, padx=PADX, pady=PADY, sticky='w')

    goalDivider = Label(root, text="------------------------------------").grid(    row=9,   column=0,  columnspan=5, padx=PADX, pady=PADY)    

    #-----# logging progress
    logNameLabel = Label(root, text="Name:").grid(                                  row=11,  column=0,  columnspan=1, padx=PADX, pady=PADY, sticky='w')
    logNameEntry = Entry(root, width=24)
    logNameEntry.grid(                                                              row=11,  column=2,  columnspan=3, padx=PADX, pady=PADY, sticky='w')

    logTimePrefix = Label(root, text="Time:").grid(                                 row=12,  column=0,  columnspan=1, padx=PADX, pady=PADY, sticky='w')
    logTimeEntry = Entry(root, width=5)
    logTimeEntry.grid(                                                              row=12,  column=2,  columnspan=1, padx=PADX, pady=PADY, sticky='w')
    logTimeSuffix = Label(root, text="minutes").grid(                               row=12,  column=3,  columnspan=2, padx=PADX, pady=PADY, sticky='w')

    #-----# button handling
    #-# functions
    def addSubject():
        subjectName = addNameEntry.get()

        logged[subjectName] = [0, 0]
        addToTable(subjectName)

        print(f"<{subjectName}> was added to the log as a new subject.")

    def setGoal():
        subjectName = goalNameEntry.get()
        goalTime = int(goalTimeEntry.get())

        if subjectName == "All":
            for item in logged:
                logged[item][1] = goalTime

        else:
            logged[subjectName][1] = goalTime

        updateTable(subjectName)

        print(f"<{goalTime}> minutes was set as the goal for subject <{subjectName}>.")

    def logProgress():
        subjectName = logNameEntry.get()
        logTime = int(logTimeEntry.get())

        logged[subjectName][0] += logTime
        updateTable(subjectName)

        print(f"<{logTime}> minutes were logged for subject <{subjectName}>")

    #-# widgets
    addButton = Button(root, text="ADD", command = addSubject)
    addButton.grid(                                                                 row=2,   column=0,  rowspan=2, columnspan=5, padx=PADX, pady=PADY)
    addButton.config(width=12)

    setButton = Button(root, text="SET", command = setGoal)
    setButton.grid(                                                                 row=8,   column=0,  columnspan=5, padx=PADX, pady=PADY)
    setButton.config(width=12)

    logButton = Button(root, text="LOG", command = logProgress)
    logButton.grid(                                                                 row=13,  column=0,  columnspan=5, padx=PADX, pady=PADY)
    logButton.config(width=12)

    return root

def main():
    logged = readLogged()

    global rowNum
    rowNum = 1 

    print(f"These are the current logged subjects. <{logged}>")

    root = setupGUI(logged)
    
    root.mainloop()

    print(f"This is the new subject log. <{logged}>")

    print("Saving to file...")
    writeLogged(logged)
    print("Saved. Enjoy!")

if __name__ == "__main__":
    main()
    