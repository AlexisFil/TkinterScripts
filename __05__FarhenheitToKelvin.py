from tkinter import *
from tkinter import ttk

def calculate(*args):
	try:
		value = float(far.get())
		kelvin.set(((value - 32)/1.8000)+273.15)
	except ValueError:
		pass

root = Tk()
root.title("Temperature Fahrenheit to Kelvin")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

far = StringVar()
kelvin = StringVar()

far_entry = ttk.Entry(mainframe, width=7, textvariable=far)
far_entry.grid(column=2, row=1,sticky=(W, E))

ttk.Label(mainframe, textvariable=kelvin).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text ='°F').grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4,sticky=W)
ttk.Label(mainframe, text ='is equivalent to').grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text ='K').grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text ='Kelvin is an absolute unit').grid(column=1,row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

far_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()

