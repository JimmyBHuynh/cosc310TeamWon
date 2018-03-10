#install tkinter http://www.tkdocs.com/tutorial/install.html
from tkinter import *
root = Tk()
root.title("NLP to Graph Queris")

# Variables
title = Label(text="Natural Language Processing into graph queries", font=("Times New Roman", 20))
desc = Label(text="Write an english sentence", font=("Times New Roman", 10))
entry_field = Entry()
button1 = Button(text="Submit",  bg="red")

def hello():
    print ('loads database to see')
menubar = Menu(root)

menubar.add_command(label="Database", command=hello)
root.config(menu=menubar)


#Postion
title.grid(column=0, row=0)
desc.grid(column=0, row=1)
entry_field.grid(column=0, row=2)
button1.grid(column=0, row=3)



#Screen
root.mainloop()
