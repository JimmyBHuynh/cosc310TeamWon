import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

phrase = input("Query: ").lower()
tokens = nltk.word_tokenize(phrase)
print(tokens)

def query5(tokens):
    var = "\"" + tokens[-2].upper() + "\""
    if ("starts" or "start") and "with" in tokens:
        query = "Match (n) : WHERE n.name STARTS WITH " + var + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    elif ("ends" or "end") and "with" in tokens:
        query = "Match (n) : WHERE n.name ENDS WITH " + var + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    elif "contains" or "contain" in tokens:
        query = "Match (n) : WHERE n.name CONTAINS " + var + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    else:
        return print("Query doesn't match templates.");

def query6(tokens):
    var2 = tokens[-2]
    if "over" in tokens:
        query = "Match (n) : WHERE n.bounty > " + var2 + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    elif ("greater" in tokens and "equal" not in tokens) or (">" in tokens and "=" not in tokens):
        query = "Match (n) : WHERE n.bounty > " + var2 + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    elif "under" in tokens:
        query = "Match (n) : WHERE n.bounty < " + var2 + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    elif ("less" in tokens and "equal" not in tokens) or ("<" in tokens and "=" not in tokens):
        query = "Match (n) : WHERE n.bounty < " + var2 + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    elif ("equals" or "equal") in tokens:
        query = "Match (n) : WHERE n.bounty = " + var2 + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    elif ("equals" or "equal") and "greater" in tokens:
        query = "Match (n) : WHERE n.bounty >= " + var2 + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    elif ("=" and ">") in tokens:
        query = "Match (n) : WHERE n.bounty >= " + var2 + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    elif ("equals" or "equal") and "less" in tokens:
        query = "Match (n) : WHERE n.bounty <= " + var2 + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    elif ("<" and "=") in tokens:
        query = "Match (n) : WHERE n.bounty <= " + var2 + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    elif ("equals" or "equal") and "not" in tokens:
        query = "Match (n) : WHERE n.bounty <> " + var2 + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    else:
        return print("Query doesn't match templates.");

if (("starts" or "start" or "ends" or "end") and "with") or ("contains" or "contain") in tokens:
    query5(tokens);
elif ("greater" or "less" or "equals" or "equal" or "over" or "under" or ">" or "<" or "=") in tokens:
    query6(tokens);