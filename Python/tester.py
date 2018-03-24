import parse
import QueryDB

myConnection = QueryDB.connection("bolt://localhost:7687","neo4j","test")

infile = open("testQueries.txt", "r")
translations = []
results = []
for line in infile:
    translations.append(parse.init(line.strip()))
for line in translations:    
    results.append(myConnection.run_Return_Query(line).strip())
infile.close

infile = open("testResults.txt", "r")
answers = []
for line in infile:
    answers.append(line.strip())
for i in range(0, len(answers)):    
    if (answers[i] == results[i]):
        print("Querie ", i, " successful")
    else:
        print("Querie ", i, " failed!")
        print("\tExpected:\t", answers[i])
        print("\tActual:\t", results[i])
infile.close
