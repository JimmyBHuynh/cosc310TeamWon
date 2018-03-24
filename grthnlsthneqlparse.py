import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#take input and convert it to a list of individual words/numbers/punctuation
phrase = input("Query: ").lower()
tokens = nltk.word_tokenize(phrase)
print(tokens)

#find the second to last element of the list (ie. the number we want)
tag = nltk.pos_tag(tokens)
print(tag)
var2 = tokens[-2]

#find corresponding template and print query desired
var2 = tokens[-2]
if "over" in tokens:
    query = "Match (n) WHERE n.bounty > " + var2 + " RETURN COUNT (n.name)"
    print(query);
if ("greater" in tokens):
    if ("equal" not in tokens):
        query = "Match (n) WHERE n.bounty > " + var2 + " RETURN COUNT (n.name)"
        print(query);
    elif ("equal" in tokens):
        query = "Match (n) WHERE n.bounty >= " + var2 + " RETURN COUNT (n.name)"
        print(query);
if "under" in tokens:
    query = "Match (n) WHERE n.bounty < " + var2 + " RETURN COUNT (n.name)"
    print(query);
if ("less" in tokens):
    if ("equal" not in tokens):
        query = "Match (n) WHERE n.bounty < " + var2 + " RETURN COUNT (n.name)"
        print(query);
    elif ("equal" in tokens):
        query = "Match (n) WHERE n.bounty <= " + var2 + " RETURN COUNT (n.name)"
        print(query);
if (("equal" or "equals") in tokens) and (("greater" and "less" and "not") not in tokens):
    query = "Match (n) WHERE n.bounty = " + var2 + " RETURN COUNT (n.name)"
    print(query);
elif ("not" in tokens) and ("equals" in tokens or "equal" in tokens):
    query = "Match (n) WHERE n.bounty <> " + var2 + " RETURN COUNT (n.name)"
    print(query);
else:
    print("Doesn't match templates. Try again.")