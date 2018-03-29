import unittest
import string

def setOutput(input):
    special = set(string.punctuation)
    #wordList = re.sub("[^\w]", " ",  input).split()
    if any(char in special for char in input):
        return "Invalid"
    else:
        return "Valid"

class GUITest( unittest.TestCase ):
    def test_gui(self):
        phrase = "Hi there"
        final = "Valid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui2(self):
        phrase = "get nodes where bounties is greater than or equal to 5000"
        final = "Valid"
        self.assertEqual(setOutput(phrase), final);    
    def test_gui3(self):
        phrase = "get nodes where bounties is >= 5000"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui4(self):
        phrase = "get nodes where bounties is less than or equal to 5000"
        final = "Valid"
        self.assertEqual(setOutput(phrase), final);    
    def test_gui5(self):
        phrase = "get nodes where bounties is <= 5000"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);  
    def test_gui6(self):
        phrase = "get nodes where bounties is equal to 5000"
        final = "Valid"
        self.assertEqual(setOutput(phrase), final);    
    def test_gui7(self):
        phrase = "get nodes where bounties is = 5000"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);    
    def test_gui8(self):
        phrase = "How many names start with J?"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui9(self):
        phrase = "This is invalid!"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui10(self):
        phrase = "get nodes where bounties is equal to $5000"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui11(self):
        phrase = "get # if nodes where names start with J"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui12(self):
        phrase = "Lets use a @"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui13(self):
        phrase = "Lets use a %"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui14(self):
        phrase = "Lets use a ^"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui15(self):
        phrase = "get names that start with J & A"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui16(self):
        phrase = "Lets use a *"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui17(self):
        phrase = "Lets use a ("
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui18(self):
        phrase = "Lets use a )"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui19(self):
        phrase = "get bounties less than 5000 - 3000"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui20(self):
        phrase = "get bounties less than 5000 + 3000"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui21(self):
        phrase = "get bounties less than 5000 + 3000"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui22(self):
        phrase = "let us use a ["
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui23(self):
        phrase = "let us use a ]"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui24(self):
        phrase = "let us use a {"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui25(self):
        phrase = "let us use a }"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui26(self):
        phrase = "let us use a ;"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui27(self):
        phrase = "let us use a :"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui28(self):
        phrase = "let us use a /"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui29(self):
        phrase = "let's use a "
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui30(self):
        phrase = "let us use a ~"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui31(self):
        phrase = "let us use a `"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui32(self):
        phrase = "let us use a ,"
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    def test_gui33(self):
        phrase = "let us use a ."
        final = "Invalid"
        self.assertEqual(setOutput(phrase), final);
    
if __name__ == '__main__':
    unittest.main()