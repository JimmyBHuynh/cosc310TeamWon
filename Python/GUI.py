from tkinter import *
import parse
import query3
import QueryDB

def setOutput(input, cypher, output, myConnection):

	#wordList = input.split()
	cypherTranslation = parse.init(input)
	print("test" ,cypherTranslation)
	#cypherTranslation = query3.query3(input)
	cypher.set(cypherTranslation)
	output.set(myConnection.run_Return_Query(cypherTranslation))



def init():
	test = QueryDB.connection("bolt://localhost:7687","neo4j","test")

	page = Tk()

	cypher = StringVar()
	output = StringVar()


	page.title("NLP Input")
	page.geometry("400x300")

	app = Frame(page)
	app.grid()

	btn1 = Button(app, text="Submit", command = lambda: setOutput(e1.get(), cypher, output,test))

	lbl1 = Label(app, text="Enter your search: ")
	lbl2 = Label(app, text="Query in Cypher: ")
	lbl3 = Label(app, textvariable=cypher)
	lbl4 = Label(app, text="Query result: ")
	lbl5 = Label(app, textvariable=output)



	e1 = Entry(app)

	lbl1.grid(row=0)
	lbl2.grid(row=2)

	e1.grid(row=0, column = 1)
	lbl3.grid(row=2, column = 1)

	btn1.grid(row = 0, column = 2, padx=10, pady=10)

	lbl4.grid(row=3, column = 0)
	lbl5.grid(row=3, column = 1)

	page.mainloop()

