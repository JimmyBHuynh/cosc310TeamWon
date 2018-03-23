import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import unittest

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
    
class FunctionTests(unittest.TestCase):
    def test_query6(self):
        phrase = ("how many bounties are over 3000?")
        tokens = nltk.word_tokenize(phrase)
        final = "Match (n) : WHERE n.bounty > 3000 RETURN COUNT (n.name)"
        self.assertEqual(query6(tokens), final);
        
if __name__ == '__main__':
    unittest.main()
