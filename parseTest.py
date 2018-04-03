import parse
import unittest
import nltk

class ParseTest( unittest.TestCase ):

    def testLabel( self ):
         
        phrase = "Get names"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n :name)\nRETURN n"
        self.assertEqual( parse.parse( tag ), compare )

    def testPropOfLabel( self ):

        phrase = "Get species of animals"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (s :animal)\nRETURN s.species"
        self.assertEqual( parse.parse( tag ), compare )

    def testCertainProp( self ):
        
        phrase = "Get nodes where species is dog"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n {species : 'dog'})\nRETURN n"
        self.assertEqual( parse.parse( tag ), compare )

    def testGr1( self ):
        
        phrase = "Get salaries greater than 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary > 100000\nRETURN n.salary"
        self.assertEqual( parse.parse( tag ), compare )

    def testGr2( self ):
        
        phrase = "Get names where salaries is greater than 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary > 100000\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testGrC1( self ):
        
        phrase = "Get count of salaries greater than 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary > 100000\nRETURN COUNT (n.salary)"
        self.assertEqual( parse.parse( tag ), compare )

    def testGrC2( self ):
        
        phrase = "Get count of names where salaries is greater than 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary > 100000\nRETURN COUNT (n.name)"
        self.assertEqual( parse.parse( tag ), compare )

    def testGrE1( self ):

        phrase = "Get names where salaries is greater than or equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary >= 100000\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testGrE2( self ):

        phrase = "Get salaries greater than or equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary >= 100000\nRETURN n.salary"
        self.assertEqual( parse.parse( tag ), compare )

    def testGrEC1( self ):

        phrase = "Get count of names where salaries is greater than or equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary >= 100000\nRETURN COUNT (n.name)"
        self.assertEqual( parse.parse( tag ), compare )

    def testGrEC2( self ):

        phrase = "Get count salaries greater than or equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary >= 100000\nRETURN COUNT (n.salary)"
        self.assertEqual( parse.parse( tag ), compare )

    def testLe1( self ):

        phrase = "Get names where salaries is less than 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary < 100000\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testLe2( self ):

        phrase = "Get salaries less than 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary < 100000\nRETURN n.salary"
        self.assertEqual( parse.parse( tag ), compare )

    def testLeC1( self ):

        phrase = "Get count of names where salaries is less than 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary < 100000\nRETURN COUNT (n.name)"
        self.assertEqual( parse.parse( tag ), compare )

    def testLeC2( self ):

        phrase = "Get count of salaries less than 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary < 100000\nRETURN COUNT (n.salary)"
        self.assertEqual( parse.parse( tag ), compare )

    def testLeE1( self ):

        phrase = "Get names where salaries is less than or equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary <= 100000\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testLeE2( self ):

        phrase = "Get salaries less than or equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary <= 100000\nRETURN n.salary"
        self.assertEqual( parse.parse( tag ), compare )

    def testLeEC1( self ):

        phrase = "Get count of names where salaries is less than or equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary <= 100000\nRETURN COUNT (n.name)"
        self.assertEqual( parse.parse( tag ), compare )

    def testLeEC2( self ):

        phrase = "Get count of salaries less than or equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary <= 100000\nRETURN COUNT (n.salary)"
        self.assertEqual( parse.parse( tag ), compare )

    def testE1( self ):

        phrase = "Get names where salaries is equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary = 100000\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testE2( self ):

        phrase = "Get salaries equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary = 100000\nRETURN n.salary"
        self.assertEqual( parse.parse( tag ), compare )

    def testEC1( self ):

        phrase = "Get count of names where salaries is equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary = 100000\nRETURN COUNT (n.name)"
        self.assertEqual( parse.parse( tag ), compare )

    def testEC2( self ):

        phrase = "Get count of salaries equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary = 100000\nRETURN COUNT (n.salary)"
        self.assertEqual( parse.parse( tag ), compare )
        
    def testNotE1( self ):

        phrase = "Get names where salaries is not equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary <> 100000\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testNotE2( self ):

        phrase = "Get salaries not equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary <> 100000\nRETURN n.salary"
        self.assertEqual( parse.parse( tag ), compare )

    def testNotEC1( self ):

        phrase = "Get count of names where salaries is not equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary <> 100000\nRETURN COUNT (n.name)"
        self.assertEqual( parse.parse( tag ), compare )

    def testNotEC2( self ):

        phrase = "Get count of salaries not equal to 100000"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.salary <> 100000\nRETURN COUNT (n.salary)"
        self.assertEqual( parse.parse( tag ), compare )

    def testStart1( self ):
        
        phrase = "Get nodes where names starts with j"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name STARTS WITH \"j\"\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testStart2( self ):
        
        phrase = "Get names starting with j"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name STARTS WITH \"j\"\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testStartC1( self ):
        
        phrase = "Get count of nodes where names start with j"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name STARTS WITH \"j\"\nRETURN COUNT (n.name)"
        self.assertEqual( parse.parse( tag ), compare )

    def testStartC2( self ):
        
        phrase = "Get count of names starting with j"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name STARTS WITH \"j\"\nRETURN COUNT (n.name)"
        self.assertEqual( parse.parse( tag ), compare )

    def testEnd1( self ):
        
        phrase = "Get nodes where names ends with j"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name ENDS WITH \"j\"\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testEnd2( self ):
        
        phrase = "Get names ending with j"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name ENDS WITH \"j\"\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testEndC1( self ):
        
        phrase = "Get count of nodes where names ends with j"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name ENDS WITH \"j\"\nRETURN COUNT (n.name)"
        self.assertEqual( parse.parse( tag ), compare )

    def testEndC2( self ):
        
        phrase = "Get count of names ending with j"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name ENDS WITH \"j\"\nRETURN COUNT (n.name)"
        self.assertEqual( parse.parse( tag ), compare )
        
    def testContain1( self ):

        phrase = "Get names containing j"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name CONTAINS \"j\"\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testContain1( self ):

        phrase = "Get nodes where names contains j"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name CONTAINS \"j\"\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testContainC1( self ):

        phrase = "Get count of names containing j"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name CONTAINS \"j\"\nRETURN COUNT (n.name)"
        self.assertEqual( parse.parse( tag ), compare )

    def testContain1( self ):

        phrase = "Get count of nodes where names contains j"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name CONTAINS \"j\"\nRETURN COUNT (n.name)"
        self.assertEqual( parse.parse( tag ), compare )



    def testNotNull( self ):
        
        phrase = "Get nodes where names is not null"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name IS NOT NULL\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )
    
    def testNotNull( self ):
        
        phrase = "Get nodes where names is null"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH (n)\nWHERE n.name IS NULL\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testanyRelQuery( self ):

        phrase = "get names of nodes that have brothers"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH () -[:brother] -> (n)\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testanyRelQueryOrder( self ):
        
        phrase = "get names of nodes that have brothers order by size"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH () -[:brother] -> (n)\nRETURN n.name ORDER BY (n.size)"
        self.assertEqual( parse.parse( tag ), compare )

    def testpropRelQuery( self ):

        phrase = "get names of nodes that have brothers where source has name joe"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH ({name : 'joe'})\n-[:brother]-> (n)\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testpropRelQuery2( self ):
        
        phrase = "get names of nodes that have brothers up to 2 hops where source has name joe"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH ({name : 'joe'})\n-[:brother *2]-> (n)\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testpropRelQuery3( self ):
        
        phrase = "get names of nodes that have brothers up to all hops where source has name joe"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH ({name : 'joe'})\n-[:brother *]-> (n)\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testpropRelQuery4( self ):
        
        phrase = "get names of nodes that have brothers between 2 to 4 hops where source has name joe"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH ({name : 'joe'})\n-[:brother *2..4]-> (n)\nRETURN n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testpropRelQuery5( self ):

        phrase = "get distinct names of nodes that have brothers where source has name joe"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH ({name : 'joe'})\n-[:brother]-> (n)\nRETURN DISTINCT n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testpropRelQuery6( self ):
        
        phrase = "get distinct names of nodes that have brothers up to 2 hops where source has name joe"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH ({name : 'joe'})\n-[:brother *2]-> (n)\nRETURN DISTINCT n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testpropRelQuery7( self ):
        
        phrase = "get distinct names of nodes that have brothers up to all hops where source has name joe"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH ({name : 'joe'})\n-[:brother *]-> (n)\nRETURN DISTINCT n.name"
        self.assertEqual( parse.parse( tag ), compare )

    def testpropRelQuery8( self ):
        
        phrase = "get distinct names of nodes that have brothers between 2 to 4 hops where source has name joe"
        tokens = nltk.word_tokenize( phrase.lower() )
        tag = nltk.pos_tag( tokens )
        compare = "MATCH ({name : 'joe'})\n-[:brother *2..4]-> (n)\nRETURN DISTINCT n.name"
        self.assertEqual( parse.parse( tag ), compare )
        
if __name__ == '__main__':
    
    unittest.main()
