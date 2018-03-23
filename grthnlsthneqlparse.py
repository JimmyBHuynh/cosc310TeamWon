import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import treebank
from nltk.stem import WordNetLemmatizer

phrase = input("Query: ").lower()
tokens = nltk.word_tokenize(phrase)
print(tokens)

tag = nltk.pos_tag(tokens)
print(tag)
var2 = tokens[-2]

if "over" in tokens:
    query = "Match (n) : WHERE n.bounty > " + var2 + "\n" + "RETURN COUNT (n.name)"
    print(query)
if ("greater" in tokens and "equal" not in tokens) or (">" in tokens and "=" not in tokens):
    query = "Match (n) : WHERE n.bounty > " + var2 + "\n" + "RETURN COUNT (n.name)"
    print(query)

if "under" in tokens:
    query = "Match (n) : WHERE n.bounty < " + var2 + "\n" + "RETURN COUNT (n.name)"
    print(query)
if ("less" in tokens and "equal" not in tokens) or ("<" in tokens and "=" not in tokens):
    query = "Match (n) : WHERE n.bounty < " + var2 + "\n" + "RETURN COUNT (n.name)"
    print(query)
    
if ("equals" or "equal") in tokens:
    query = "Match (n) : WHERE n.bounty = " + var2 + "\n" + "RETURN COUNT (n.name)"
    print(query)
elif ("equals" or "equal") and "greater" in tokens:
    query = "Match (n) : WHERE n.bounty >= " + var2 + "\n" + "RETURN COUNT (n.name)"
    print(query)
elif ("=" and ">") in tokens:
    query = "Match (n) : WHERE n.bounty >= " + var2 + "\n" + "RETURN COUNT (n.name)"
    print(query)
elif ("equals" or "equal") and "less" in tokens:
    query = "Match (n) : WHERE n.bounty <= " + var2 + "\n" + "RETURN COUNT (n.name)"
    print(query)
elif ("<" and "=") in tokens:
    query = "Match (n) : WHERE n.bounty <= " + var2 + "\n" + "RETURN COUNT (n.name)"
    print(query)
elif ("equals" or "equal") and "not" in tokens:
    query = "Match (n) : WHERE n.bounty <> " + var2 + "\n" + "RETURN COUNT (n.name)"
    print(query)
elif "!" in tokens:
    query = "Match (n) : WHERE n.bounty <> " + var2 + "\n" + "RETURN COUNT (n.name)"
    print(query)