import nltk
from nltk.corpus import treebank
#Inflect engine faster than lemmatizer for singularizing words
#Depluralizing has issues with words ending in 'ies' - eg. species/specie
#import inflect
from nltk.stem import WordNetLemmatizer

#Lemmatizer
lem = WordNetLemmatizer()

keywords = "get", "count", "number", "of", "where"
query = ""

def getInput():
    #Get input --> Going to be function in itself later
        
    phrase = input( "Query: " )
    tokens = nltk.word_tokenize( phrase.lower() )

    tag = nltk.pos_tag( tokens )

    iterTag = iter( tag )

    print( tag )

    query = ""
    count = 0

    return tag

def getFirstKeyword( tag ):

    count = 0
    while tag[count][0] not in keywords:

        count = count + 1
        print( "not in keywords: " + str( tag[count][0] ) )

    print( "First keyword: " + str( tag[count][0] ) )
           
    return count

def parse( tag, idxKey ):

    query = ""

    if tag[idxKey + 1][1] == "DT":

        #Determinant handling
        print( "determinant: " )
        idxKey = idxKey + 1

    elif tag[idxKey + 1][1] == "NNS" or tag[idxKey + 1][1] == "NNPS":

        idxKey = idxKey + 1

        #Plural noun handling
        if idxKey + 1 == len( tag ):

            var = tag[idxKey][0][0]
            query = "Match(" + var + " :" + tag[idxKey][0] + ")" + "\n" + "RETURN " + var

        else:

            #Dunno, let'sl ook for next keyword
            print( "looking for next keyword" )
            idxKey = nextKeyword( tag, idxKey )
            

    print( query )
        
    return

def nextKeyword( tag, idxKey ):

    while tag[idxKey][0] not in keywords:

        idxKey = idxKey + 1

    print( "Next Keyword: " + tag[idxKey][0] )

    return idxKey

tag = getInput()
idxKey = getFirstKeyword( tag )
parse( tag, idxKey )

