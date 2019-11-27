
from tkinter import *

w =Tk()

def myClick():
    myLabel = Label(w,text = "Το κλικάρισα!!!")
    myLabel.pack()


myButton = Button(w, text = "Κλίκ!",padx ='50',pady='50',command = myClick,bg = 'teal')
#,state = DISABLED (μετά το text για απενεργοποίηση :) 

myButton.pack()
w.mainloop()

