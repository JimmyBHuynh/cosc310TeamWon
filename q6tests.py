import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import unittest

#For testing \n was removed. Having RETURN... on the same line will output the same result in Cypher.

def query6(tokens):
    var2 = tokens[-2]
    if "over" in tokens:
        query = "Match (n) WHERE n.bounty > " + var2 + " RETURN COUNT (n.name)"
        return query;
    if ("greater" in tokens):
        if ("equal" not in tokens):
            query = "Match (n) WHERE n.bounty > " + var2 + " RETURN COUNT (n.name)"
            return query;
        elif ("equal" in tokens):
            query = "Match (n) WHERE n.bounty >= " + var2 + " RETURN COUNT (n.name)"
            return query;
    if "under" in tokens:
        query = "Match (n) WHERE n.bounty < " + var2 + " RETURN COUNT (n.name)"
        return query;
    if ("less" in tokens):
        if ("equal" not in tokens):
            query = "Match (n) WHERE n.bounty < " + var2 + " RETURN COUNT (n.name)"
            return query;
        elif ("equal" in tokens):
            query = "Match (n) WHERE n.bounty <= " + var2 + " RETURN COUNT (n.name)"
            return query;
    if (("equal" or "equals") in tokens) and (("greater" and "less" and "not") not in tokens):
        query = "Match (n) WHERE n.bounty = " + var2 + " RETURN COUNT (n.name)"
        return query;
    elif ("not" in tokens) and ("equals" in tokens or "equal" in tokens):
        query = "Match (n) WHERE n.bounty <> " + var2 + " RETURN COUNT (n.name)"
        return query;
    else:
        return;
                                
class FunctionTests(unittest.TestCase):
    def test_query6(self):
        phrase = ("how many bounties are over 3000?")
        tokens = nltk.word_tokenize(phrase)
        final = "Match (n) WHERE n.bounty > 3000 RETURN COUNT (n.name)"
        self.assertEqual(query6(tokens), final);
    def test_query6_2(self):
        phrase = ("how many bounties are under 3000?")
        tokens = nltk.word_tokenize(phrase)
        final = "Match (n) WHERE n.bounty < 3000 RETURN COUNT (n.name)"
        self.assertEqual(query6(tokens), final);
    def test_query6_3(self):
        phrase = ("how many bounties are greater than 3000?")
        tokens = nltk.word_tokenize(phrase)
        final = "Match (n) WHERE n.bounty > 3000 RETURN COUNT (n.name)"
        self.assertEqual(query6(tokens), final);
    def test_query6_4(self):
        phrase = ("how many bounties are less than 3000?")
        tokens = nltk.word_tokenize(phrase)
        final = "Match (n) WHERE n.bounty < 3000 RETURN COUNT (n.name)"
        self.assertEqual(query6(tokens), final);
    def test_query6_5(self):
        phrase = ("how many bounties are equal to 3000?")
        tokens = nltk.word_tokenize(phrase)
        final = "Match (n) WHERE n.bounty = 3000 RETURN COUNT (n.name)"
        self.assertEqual(query6(tokens), final);
    def test_query6_6(self):
        phrase = ("how many bounties are not equal to 3000?")
        tokens = nltk.word_tokenize(phrase)
        final = "Match (n) WHERE n.bounty <> 3000 RETURN COUNT (n.name)"
        self.assertEqual(query6(tokens), final);
    def test_query6_7(self):
        phrase = ("how many bounties are greater than or equal to 3000?")
        tokens = nltk.word_tokenize(phrase)
        final = "Match (n) WHERE n.bounty >= 3000 RETURN COUNT (n.name)"
        self.assertEqual(query6(tokens), final);
    def test_query6_8(self):
        phrase = ("how many bounties are less than or equal to 3000?")
        tokens = nltk.word_tokenize(phrase)
        final = "Match (n) WHERE n.bounty <= 3000 RETURN COUNT (n.name)"
        self.assertEqual(query6(tokens), final);
        
if __name__ == '__main__':
    unittest.main()
