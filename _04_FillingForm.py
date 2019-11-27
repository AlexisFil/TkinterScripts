
from tkinter import *

w =Tk()

e= Entry(w,width = 50 , borderwidth = 10)
e.pack()
e.insert(0,'Πάιχτης 1')

def myClick():
    myLabel = Label(w,text ='Ο/Η ' + e.get()+ ' νίκησε!!!')
    myLabel.pack()


myButton = Button(w, text = "Νίκη",padx ='20',pady='20',command = myClick,bg = 'green')
#,state = DISABLED (μετά το text για απενεργοποίηση :) 

myButton.pack()
w.mainloop()

