from tkinter import *

w =Tk()

#label widget 1.defune 2.put onto screen
Label1 = Label(w, text="Γειά σας!!!")
Label2 = Label(w, text="Με λένε Αλέξη.")
Label3 = Label(w, text="Έχω ύψος 1.84 m.")

Label1.grid(row=0, column = 0)
Label2.grid(row=1, column = 1)
Label3.grid(row=2, column = 5)

w.mainloop()

