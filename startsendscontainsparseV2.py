import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#take input and convert it to a list of individual words/numbers/punctuation
phrase = input("Query: ").lower()
tokens = nltk.word_tokenize(phrase)
print(tokens)

#find the second to last element of the list (ie. the letter we want)
tag = nltk.pos_tag(tokens)
print(tag)
var = "\"" + tokens[-2].upper() + "\""

#find corresponding template and print query desired
if "starting" in tokens:
    query = "Match (n) WHERE n.name STARTS WITH " + var + "\n" + "RETURN COUNT (n.name)"
    print(query);
elif "start" in tokens:
    query = "Match (n) WHERE n.name STARTS WITH " + var + "\n" + "RETURN COUNT (n.name)"
    print(query);
elif "ending" in tokens:
    query = "Match (n) WHERE n.name ENDS WITH " + var + "\n" + "RETURN COUNT (n.name)"
    print(query)
elif "end" in tokens:
    query = "Match (n) WHERE n.name ENDS WITH " + var + "\n" + "RETURN COUNT (n.name)"
    print(query)
elif "containing" in tokens:
    query = "Match (n) WHERE n.name CONTAINS " + var + "\n" + "RETURN COUNT (n.name)"
    print(query)
elif "contain" in tokens:
    query = "Match (n) WHERE n.name CONTAINS " + var + "\n" + "RETURN COUNT (n.name)"
    print(query)
else:
    print("Query doesn't match. Try saying it differently. Remember to add a ? at the end.")

