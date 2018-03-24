import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import unittest

#For testing \n was removed. Having RETURN... on the same line will output the same result in Cypher.

def query5(tokens):
    var = "\"" + tokens[-2].upper() + "\"";
    if "start" in tokens:
        query = "Match (n) WHERE n.name STARTS WITH " + var + " RETURN COUNT (n.name)"
        return query;
    elif "starting" in tokens:
        query = "Match (n) WHERE n.name STARTS WITH " + var + " RETURN COUNT (n.name)"
        return query;
    elif "end" in tokens:
        query = "Match (n) WHERE n.name ENDS WITH " + var + " RETURN COUNT (n.name)"
        return query;
    elif "ending" in tokens:
        query = "Match (n) WHERE n.name ENDS WITH " + var + " RETURN COUNT (n.name)"
        return query;
    elif "contain" in tokens:
        query = "Match (n) WHERE n.name CONTAINS " + var + " RETURN COUNT (n.name)"
        return query;
    elif "containing" in tokens:
        query = "Match (n) WHERE n.name CONTAINS " + var + " RETURN COUNT (n.name)"
        return query;
    else:
        return;

class FunctionTests(unittest.TestCase):
    def test_query5(self):
        phrase1 = ("how many names start with J?")
        tokens1 = nltk.word_tokenize(phrase1)
        final1 = 'Match (n) WHERE n.name STARTS WITH ' + '\"'+ 'J' + '\"' + ' RETURN COUNT (n.name)'
        self.assertEqual(query5(tokens1), final1);
    def test_query5_2(self):
        phrase2 = ("how many names end with A?")
        tokens2 = nltk.word_tokenize(phrase2)
        final2 = 'Match (n) WHERE n.name ENDS WITH ' + '\"'+ 'A' + '\"' + ' RETURN COUNT (n.name)'
        self.assertEqual(query5(tokens2), final2);
    def test_query5_3(self):
        phrase3 = ("how many names contain E?")
        tokens3 = nltk.word_tokenize(phrase3)
        final3 = 'Match (n) WHERE n.name CONTAINS ' + '\"'+ 'E' + '\"' + ' RETURN COUNT (n.name)'
        self.assertEqual(query5(tokens3), final3);
    def test_query5_4(self):
        phrase1 = ("how many names are there starting with K?")
        tokens1 = nltk.word_tokenize(phrase1)
        final1 = 'Match (n) WHERE n.name STARTS WITH ' + '\"'+ 'K' + '\"' + ' RETURN COUNT (n.name)'
        self.assertEqual(query5(tokens1), final1);
    def test_query5_5(self):
        phrase2 = ("how many names are there ending with B?")
        tokens2 = nltk.word_tokenize(phrase2)
        final2 = 'Match (n) WHERE n.name ENDS WITH ' + '\"'+ 'B' + '\"' + ' RETURN COUNT (n.name)'
        self.assertEqual(query5(tokens2), final2);
    def test_query5_6(self):
        phrase3 = ("how many names are there containing F?")
        tokens3 = nltk.word_tokenize(phrase3)
        final3 = 'Match (n) WHERE n.name CONTAINS ' + '\"'+ 'F' + '\"' + ' RETURN COUNT (n.name)'
        self.assertEqual(query5(tokens3), final3);
        
if __name__ == '__main__':
    unittest.main()
