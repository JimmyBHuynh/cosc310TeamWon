from tkinter import *
import re
import string

def setOutput(input):
    special = set(string.punctuation)
    wordList = re.sub("[^\w]", " ",  input).split()
    if any(char in special for char in input):
        output.set("Special characters invalid. Please try again.")
    else:
        output.set(wordList)

page = Tk()

output = StringVar()

page.title("NLP Input")
page.geometry("400x200")

app = Frame(page)
app.grid()

e1 = Entry(app)

btn1 = Button(app, text="Submit", command = lambda: setOutput(e1.get()))

lbl1 = Label(app, text="Enter your search: ")
lbl2 = Label(app, text="Query in Cypher: ")
lbl3 = Label(app, textvariable=output)


lbl1.grid(row=0)
lbl2.grid(row=2)

e1.grid(row=0, column = 1)
lbl3.grid(row=2, column = 1)

btn1.grid(row = 0, column = 2, padx=10, pady=10)

page.mainloop()
