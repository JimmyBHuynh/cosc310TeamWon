from tkinter import *
import parse
import query3
import QueryDB
import sys

def setOutput(input, cypher, output, myConnection):

	#wordList = input.split()
	try:
		cypherTranslation = parse.init(input)
	except:
		cypherTranslation = "Error in translating step"
	#cypherTranslation = query3.query3(input)
	if(not cypherTranslation):
		cypherTranslation = "Error in translating step"
		cypher.set(cypherTranslation)
	else:
		cypher.set(cypherTranslation)
		outputValue = str(myConnection.run_Return_Query(cypherTranslation))
		if (not outputValue):
			output.set("The query did not return a result, is this data in the database?")
		else:	
			output.set(outputValue)



def init():
	try:
		test = QueryDB.connection("bolt://localhost:7687","neo4j","test")
	except:
		print("Cannot connect to server")
		sys.exit()


	page = Tk()

	cypher = StringVar()
	output = StringVar()


	page.title("NLP Input")
	page.geometry("700x350")

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

