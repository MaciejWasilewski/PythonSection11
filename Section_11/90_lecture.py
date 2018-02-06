import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8
buttons = []
buttonTexts = list(map(str, list(range(0, 10, 1))))
buttonTexts.append('=')
buttonTexts.append('/')
buttonTexts.append('*')
buttonTexts.append('-')
buttonTexts.append('+')
buttonTexts.append('C')
buttonTexts.append('CE')
buttonCols = [0, 0, 1, 2, 0, 1, 2, 0, 1, 2, 1, 3, 3, 3, 3, 0, 1]
buttonRows = [5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 5, 5, 4, 3, 2, 1, 1]
result=tkinter.Entry(mainWindow)
result.grid(row=0, column=0, columnspan=5, sticky='nsew')
print(buttonTexts)
for i in range(len(buttonTexts)):
    print(buttonTexts[i])
    buttons.append(tkinter.Button(mainWindow, text=buttonTexts[i]))
    buttons[i].grid(row=buttonRows[i], column=buttonCols[i], sticky='nswe')
buttons[10].grid(row=buttonRows[10], column=buttonCols[10], sticky='nswe',columnspan=2)
mainWindow.mainloop()
