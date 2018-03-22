import nltk
from nltk.corpus import treebank
#Inflect engine faster than lemmatizer for singularizing words
#Depluralizing has issues with words ending in 'ies' - eg. species/specie
#import inflect
from nltk.stem import WordNetLemmatizer

#Lemmatizer
lem = WordNetLemmatizer()
keywords = "get", "count", "number", "where", "and", "is", "and"
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

def singular( word ):

    plural = word
    toSing = lem.lemmatize( word )

    if toSing[len( toSing ) - 2: len( toSing )] =="ie":
        return plural
    else:
        return toSing

def getFirstKeyword( tag ):

    count = 0
    while tag[count][0] not in keywords:

        count = count + 1

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
        prop = singular( tag[idxKey][0] )
        var = tag[idxKey][0][0]

        #Plural noun handling
        if idxKey + 1 == len( tag ):

            var = tag[idxKey][0][0]
            query = "Match(" + var + " :" + tag[idxKey][0] + ")" + "\n" + "RETURN " + var
            
            
        else:

            #Dunno, let's look for next keyword
            print( "looking for next keyword" )
            idxKey = nextKeyword( tag, idxKey )
            queryPart = handleKeyword( tag, idxKey )
            query = "Match(" + var + " :" + queryPart + ")" + "\n" + "RETURN " + var + "." + prop
    else:

        idxKey = idxKey + 1
        print( "outter loop. Looking for next keyword: " )
        idxKey = nextKeyword( tag, idxKey )
        query = handleKeyword( tag, idxKey )
            
    print( query )
        
    return

def nextKeyword( tag, idxKey ):

    while tag[idxKey][0] not in keywords and idxKey < len( tag )-1:

        idxKey = idxKey + 1

    print( "Next Keyword: " + tag[idxKey][0] )

    return idxKey

def handleKeyword( tag, idxKey ):

    keyword = tag[idxKey][0]
    keyTag = tag[idxKey][1]
    queryPart = ""


    #bunch of ifs yo
    if keyword == "count":

        print()
        
    elif keyword == "where":

        count = 1
        nextTag = tag[idxKey + count][1]
        if nextTag == "NNS" or nextTag == "NNPS":
            
            prop = singular( tag[idxKey + 1][0] )
            print( prop )

            count = count + 1
            
            if tag[idxKey + count][0] == "is":

                count = count + 1
                nextWord = tag[idxKey + count]

                if nextWord[1] == "JJ":

                    queryPart = "Match (n {" + prop + " : '" + nextWord[0] + "'})" + "\n" + "RETURN n"  

    elif keyword == "and":

        print()
        bef = tag[idxKey - 1][0]
        befTag = tag[idxKey - 1][1]
        aft = tag[idxKey + 1][0]
        aftTag = tag[idxKey + 1][0]
        
        if befTag == "NNS" or befTag == "NNPS":
            bef = singular( bef )
        if aftTag == "NNS" or aftTag == "NNPS":
            aft = singular( aft )
        
        #If plural - singularize
        #Label conjunction if we find 'and'?
        queryPart = bef + " :" + aft

    elif keyTag == "NNPS" or keyTag == "NNS":

        queryPart = singular( tag[idxKey][0] )
        

    return queryPart

tag = getInput()
idxKey = getFirstKeyword( tag )
parse( tag, idxKey )

