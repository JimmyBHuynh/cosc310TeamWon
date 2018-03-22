import nltk
from nltk.corpus import treebank
#Inflect engine faster than lemmatizer for singularizing words
#Depluralizing has issues with words ending in 'ies' - eg. species/specie
#import inflect
from nltk.stem import WordNetLemmatizer

#Lemmatizer
lem = WordNetLemmatizer()
keywords = "get", "count", "number", "where", "and", "is", "and", "starting", "ending", "containing"
query = ""
global countExist

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

def nextKeyword( tag, idxKey ):

    while tag[idxKey][0] not in keywords and idxKey < len( tag )-1:

        idxKey = idxKey + 1

    print( "Next Keyword: " + tag[idxKey][0] )

    return idxKey

def parse( tag ):

    idxKey = getFirstKeyword( tag )
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
            if tag[idxKey][0] not in keywords:
                queryPart = handleKeyword( tag, idxKey, 0 )
                query = "Match(" + var + " :" + queryPart + ")" + "\n" + "RETURN " + var + "." + prop
            else:
                query = handleKeyword( tag, idxKey, 0 )

    else:

        idxKey = idxKey + 1
        print( "outer loop. Looking for next keyword: " )
        idxKey = nextKeyword( tag, idxKey )
        query = handleKeyword( tag, idxKey, 0 )
            
    print( query )
        
    return

def handleKeyword( tag, idxKey, countExist ):

    keyword = tag[idxKey][0]
    keyTag = tag[idxKey][1]
    queryPart = ""
    #bunch of ifs yo
    exists = countExist

    if keyword == "count":

        exists = 1
        queryPart = handleKeyword( tag, nextKeyword( tag, idxKey + 1 ), 1 )
        
    elif keyword == "starting":
        
        count = 1
        prevWd = tag[idxKey - 1]
        nextWd = tag[idxKey + count]
        if prevWd[1] == "NNS" or prevWd[1] == "NNPS":
            if nextWd[0] == "with":
                count = count + 1
                if countExist == 1:
                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + prevWd[0] + " STARTS WITH " + "\"" + tag[idxKey + count][0] + "\"\n" + "RETURN COUNT (n." + prevWd[0] + ")"
                else:
                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + prevWd[0] + " STARTS WITH " + "\"" + tag[idxKey + count][0] + "\"\n" + "RETURN n." + prevWd[0]

    elif keyword == "ending":

        count = 1
        prevWd = tag[idxKey - 1]
        nextWd = tag[idxKey + count]
        if prevWd[1] == "NNS" or prevWd[1] == "NNPS":
            if nextWd[0] == "with":
                count = count + 1
                if countExist == 1:
                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + prevWd[0] + " ENDS WITH " + "\"" + tag[idxKey + count][0] +"\"\n" + "RETURN COUNT (n." + prevWd[0] + ")"
                else:
                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + prevWd[0] + " ENDS WITH " + "\"" + tag[idxKey + count][0] +"\"\n" + "RETURN n." + prevWd[0]
 
    elif keyword == "containing":

        count = 1
        prevWd = tag[idxKey - 1]
        if prevWd[1] == "NNS" or prevWd[1] == "NNPS":
            if countExist == 1:
                queryPart = "MATCH (n)" + "\n" + "WHERE n." + prevWd[0] + " CONTAINS " + "\"" + tag[idxKey + count][0] +"\"\n" + "RETURN COUNT (n." + prevWd[0] + ")"
            else:
                queryPart = "MATCH (n)" + "\n" + "WHERE n." + prevWd[0] + " CONTAINS " + "\"" + tag[idxKey + count][0] +"\"\n" + "RETURN n." + prevWd[0]
        
    elif keyword == "where":

        count = 1
        nextTag = tag[idxKey + count][1]
        if nextTag == "NN" or nextTag == "NNP" or nextTag == "NNS" or nextTag == "NNPS":
            
            prop = singular( tag[idxKey + 1][0] )

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

        #Could not find keywords.. oh oh
        queryPart = singular( tag[idxKey][0] )
        
    return queryPart

tag = getInput()
parse( tag )
