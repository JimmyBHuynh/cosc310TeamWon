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

if ("starts" or "start") and "with" in tokens:
    var = "\"" + tokens[-2].upper() + "\""
    if tag[-2][1] == "NN":
        query = "Match (n) : WHERE n.name STARTS WITH " + var + "\n" + "RETURN COUNT (n.name)"
        print(query)
    elif ("ends" or "end") and "with" in tokens:
        query = "Match (n) : WHERE n.name ENDS WITH " + var + "\n" + "RETURN COUNT (n.name)"
        print(query)
    elif ("contains" or "contain") in tokens:
        query = "Match (n) : WHERE n.name CONTAINS " + var + "\n" + "RETURN COUNT (n.name)"
        print(query)
    else:
        print("Query doesn't match. Try saying it differently. Remember to add a ? at the end.")

