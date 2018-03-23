import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import unittest

def query5(tokens):
    var = "\"" + tokens[-2].upper() + "\"";
    if ("starts" or "start") and "with" in tokens:
        query = "Match (n) : WHERE n.name STARTS WITH " + var + " RETURN COUNT (n.name)"
        return print(query);
    elif ("ends" or "end") and "with" in tokens:
        query = "Match (n) : WHERE n.name ENDS WITH " + var + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    elif "contains" or "contain" in tokens:
        query = "Match (n) : WHERE n.name CONTAINS " + var + "\n" + "RETURN COUNT (n.name)"
        return print(query);
    else:
        return print("Query doesn't match templates.");

class FunctionTests(unittest.TestCase):
    def test_query5(self):
        phrase = ("how many names start with J?")
        tokens = nltk.word_tokenize(phrase)
        final = 'Match (n) : WHERE n.name STARTS WITH ' + '\"'+ 'J' + '\"' + ' RETURN COUNT (n.name)'
        self.assertEqual(query5(tokens), final);
        
if __name__ == '__main__':
    unittest.main()
