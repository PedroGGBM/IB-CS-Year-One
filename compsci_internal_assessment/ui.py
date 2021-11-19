# from tkinter import *
# from tkinter.ttk import Combobox

# window=Tk()
# window.configure(bg='black')
# var = StringVar()
# var.set("one")
# data=("one", "two", "three", "four")
# cb=Combobox(window, values=data)
# cb.place(x=60, y=150)

# lb=Listbox(window, height=5, selectmode='multiple')
# for num in data:
#     lb.insert(END,num)
# lb.place(x=250, y=150)

# v0=IntVar()
# v0.set(1)
# r1=Radiobutton(window, text="male", variable=v0,value=1)
# r2=Radiobutton(window, text="female", variable=v0,value=2)
# r1.place(x=100,y=50)
# r2.place(x=180, y=50)
                
# v1 = IntVar()
# v2 = IntVar()
# C1 = Checkbutton(window, text = "Employee", variable = v1)
# C2 = Checkbutton(window, text = "Client", variable = v2)
# C1.place(x=100, y=100)
# C2.place(x=180, y=100)

# window.title('Archivid')
# window.geometry("400x300+10+10")
# window.mainloop()

# Import module
from tkinter import *
import math 
import random 

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Add image file
bg = PhotoImage( file = "C:\Users\Pedro Gronda\Downloads\Untitled drawing (1).jpg")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)

# Add text
label2 = Label( root, text = "Welcome",
			bg = "#88cffa")

label2.pack(pady = 50)

# Create Frame
frame1 = Frame( root, bg = "#88cffa")
frame1.pack(pady = 20)

# Add buttons
button1 = Button( frame1, text = "Exit")
button1.pack(pady = 20)

button2 = Button( frame1, text = "Start")
button2.pack(pady = 20)

button3 = Button( frame1, text = "Reset")
button3.pack(pady = 20)

# Execute tkinter
root.mainloop()
