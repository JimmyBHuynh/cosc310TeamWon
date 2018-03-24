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
var = "\"" + tokens[-2].upper() + "\""

if "their" or "theirs" in tokens:
    query = "Match (n) : WHERE THEIR n.name  " + var + "\n" + "RETURN COUNT (n.name)"
    print(query)
else:
    print("Query doesn't match. Try another way of saying it.")