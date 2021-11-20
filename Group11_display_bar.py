
import tkinter as tk
from tkinter import Entry, Label, ttk
import time
from tkinter.constants import LEFT, NE, NW, TOP

root = tk.Tk()
root.geometry('320x480')
root.config(bg='#345') #background color

#dynamic bar
progressBar = ttk.Progressbar(root, length=300, cursor='spider',
                    mode="determinate",
                    orient=tk.VERTICAL)
progressBar.grid(row=4,column=1, pady=0, sticky=NW, rowspan=5)

#Labels
titleLabel = Label(root, text="Fuel Indicator", bd=4, background='#345', font=('Helvetica', 16, 'italic', 'bold'), fg='white')
titleLabel.grid(row=1,column=0)

label1 = Label(root, text="Enter fuel (Liters): ", background='#345', font=('Helvetica', 10), fg='white')
label1.grid(row=2,column=0)

#inidcators using custom grid
indicatorsLabel = Label(root, text="100(L) -- ", background='#345', font=('Helvetica', 8), fg='white', pady=0)
indicatorsLabel.grid(row =4, column=0, sticky=NE)
indicatorsLabel = Label(root, text="80(L) --  ", background='#345', font=('Helvetica', 8), fg='white', pady=0)
indicatorsLabel.grid(row =5, column=0, sticky=NE)
indicatorsLabel = Label(root, text="60(L) --  ", background='#345', font=('Helvetica', 8), fg='white', pady=0)
indicatorsLabel.grid(row =6, column=0, sticky=NE)
indicatorsLabel = Label(root, text="40(L) --  ", background='#345', font=('Helvetica', 8), fg='white', pady=0)
indicatorsLabel.grid(row =7, column=0, sticky=NE)
indicatorsLabel = Label(root, text="20(L) --  ", background='#345', font=('Helvetica', 8), fg='white', pady=0)
indicatorsLabel.grid(row =8, column=0, sticky=NE)

indicatorsLabel = Label(root, text="20(L) --  ", background='#345', font=('Helvetica', 5), fg='#345', pady=0)
indicatorsLabel.grid(row =4, column=1, sticky=NW)


#Entry
Lenght = Entry(root, bd=2)
Lenght.grid(row=2,column=1, pady=8)

#method to handle bar
def increment(*args):
    intlenght = int(Lenght.get()) - 3 #converting and getting value + necessary offset to align with indicators
    for i in range(intlenght): #fill according to the entry number
        progressBar["value"] = i+1
        root.update()
        time.sleep(0.1)
btn = ttk.Button(root,text="Start",command=increment) #button to execute increment
btn.grid(row=3,column=1, pady=8)

root.mainloop()

