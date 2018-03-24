import nltk
#Inflect engine faster than lemmatizer for singularizing words
#Depluralizing has issues with words ending in 'ies' - eg. species/specie
#import inflect
from nltk.stem import WordNetLemmatizer

keywords = "number", "where", "and", "is", "and", "starting", "ending", "containing", "greater", "less", "equal"
query = ""

def getInput():
        
    phrase = input( "Query: " )
    tokens = nltk.word_tokenize( phrase.lower() )
    
    tag = nltk.pos_tag( tokens )

    print( tag )

    query = ""
    count = 0

    return tag

def anyRelQuery( rel, prop ):

    #Triggered by phrases like: get names that are parents
    query = "MATCH () -[:" + rel + "] -> (n)" + "\n" + "RETURN n." + prop
        
    return query

def propOfQuery( prop, label ):

    #Triggered by phrases like: get names of animals
    query = "MATCH (" + prop[0] + " :" + label + ")" + "\n" + "RETURN " + prop[0] + "." + prop

    return query

def startWithQuery( prop, string, count ):

    #Triggered by phrases like: get nodes where names starts with J
    #Triggered by phrases like: get names starting with J
    
    if count == 1:
        
        query = "MATCH (n)" + "\n" + "WHERE n." + prop + " STARTS WITH " + "\"" + string + "\"\n" + "RETURN COUNT (n." + prop + ")"

    else:

        query = "MATCH (n)" + "\n" + "WHERE n." + prop + " STARTS WITH " + "\"" + string + "\"\n" + "RETURN n." + prop
        
    return query
        
def endWithQuery( prop, string, count ):
    
    #Triggered by phrases like: get nodes where names ends with J
    #Triggered by phrases like: get names ending with J
    
    if count == 1:

        query = "MATCH (n)" + "\n" + "WHERE n." + prop + " ENDS WITH " + "\"" + string + "\"\n" + "RETURN COUNT (n." + prop + ")"
        
    else:

        query = "MATCH (n)" + "\n" + "WHERE n." + prop + " ENDS WITH " + "\"" + string + "\"\n" + "RETURN n." + prop

    return query

def containQuery( prop, string, count ):
    
    #Triggered by phrases like: get nodes where names contains J
    #Triggered by phrases like: get names containing J
    
    if count == 1:

        query = "MATCH (n)" + "\n" + "WHERE n." + prop + " CONTAINS " + "\"" + string + "\"\n" + "RETURN COUNT (n." + prop + ")"

    else:

        query = "MATCH (n)" + "\n" + "WHERE n." + prop + " CONTAINS " + "\"" + string + "\"\n" + "RETURN n." + prop

    return query

def equalityQuery( prop, prop2, amount, sign, count ):

    #Triggered by phrases like: get nodes where bounties is greater than or equal to 5000
    #Triggered by phrases like: get prices equal to 5000
    #Triggered by phrases like: get nodes where salary is not equal to 50000
    #Triggered by phrases like: get salaries equal to 100000

    if count == 1:
        
        query = "MATCH (n)" + "\n" + "WHERE n." + prop + " " + sign + " " + amount + "\n" + "RETURN COUNT (n." + prop2 + ")"

    else:

        query = "MATCH (n)" + "\n" + "WHERE n." + prop + " " + sign + " " + amount + "\n" + "RETURN n." + prop2

    return query

def nullPropQuery( prop, null, count ):

    if count == 1:

        if null == 1:

            query = "MATCH (n)" + "\n" + "WHERE n." + prop + " IS NULL" + "\n" + "RETURN COUNT (n." + prop  + ")"  

        else:

            query = "MATCH (n)" + "\n" + "WHERE n." + prop + " IS NOT NULL" + "\n" + "RETURN COUNT (n." + prop + ")"

    else:

        if null == 1:

            query = "MATCH (n)" + "\n" + "WHERE n." + prop + " IS NULL" + "\n" + "RETURN n." + prop

        else:

            query = "MATCH (n)" + "\n" + "WHERE n." + prop + " IS NOT NULL" + "\n" + "RETURN n." + prop

    return query
        
def singular( word ):

    #Turns plural nouns into their singular form.
    #Assumes databases properties are in their singular form.
    lem = WordNetLemmatizer()
    plural = word
    toSing = lem.lemmatize( word )

    if toSing[len( toSing ) - 2: len( toSing )] =="ie":
        return plural
    else:
        return toSing

def nextKeyword( tag, idxKey ):

    #Look for keywords in our list
    while tag[idxKey][0] not in keywords and idxKey < len( tag )-1:

        idxKey = idxKey + 1

    #print( "Next Keyword: " + tag[idxKey][0] )

    return idxKey

def parse( tag ):

    #initialize modifiers
    countExist = 0
    distint = 0
    order = 0

    #check if any modifiers exists, then we need to change states
    for i in range( 0, len( tag ) ):

        if tag[i][0] == "count":

            countExist = 1

        if tag[i][0] == "distinct":

            distinct = 1

        if tag[i][0] == "order":

            order = 1

    #initialize search, currently relies on get being first keyword hit
    idxKey = 0
    idxKey = nextKeyword( tag, idxKey )
    query = ""
    if tag[idxKey][0] not in keywords:
        
        idxKey = 0
        #check if the next word is a noun
        if tag[idxKey + 1][1] == "NNS" or tag[idxKey + 1][1] == "NNPS" or tag[idxKey + 1] == "NN" or tag[idxKey +1] == "NNP":

            #most likely, we found a noun after get
            idxKey = idxKey + 1
            prop = singular( tag[idxKey][0] )
            var = tag[idxKey][0][0]
            attemptLength = idxKey + 1
            #Plural noun handling
            if idxKey + 1 == len( tag ):

                var = tag[idxKey][0][0]
                query = "MATCH (" + var + " :" + singular( tag[idxKey][0] ) + ")" + "\n" + "RETURN " + var
            
            elif attemptLength < len( tag ):
            #If we find of, the previous word is a property?   
                if tag[idxKey+1][0] == "of":

                    idxKey = idxKey + 2
                    nodeLabel = tag[idxKey][0]
                    
                    #If that is not the end
                    if idxKey+1 < len( tag ):

                        #If it is that, or who
                        if tag[idxKey + 1][0] == "that" or tag[idxKey + 1][0] == "who":
                            idxKey = idxKey + 1
                            nextWd = tag[idxKey + 1]

                            #If have is after that or who, then it is a relation
                            if nextWd[0] == "have":
                                
                                idxKey = idxKey + 1
                                nextWd = tag[idxKey + 1]

                                #If the next word is a plural noun, then we matched a relational query
                                if nextWd[1] == "NNS" or nextWd[1] == "NNPS":

                                    if order == 1:

                                        lastWd = tag[len( tag )-1]
                                        
                                        if lastWd[1] == "NN" or lastWd[1] == "NNP":
                                            
                                            #get names that are parents order by size
                                            query = "MATCH () -[:" + nextWd[0] + "] -> (n)" + "\n" + "RETURN n." + prop + " ORDER BY n." + lastWd[0]
                                            
                                    else:
                                        
                                        #get names that are parents
                                        query = anyRelQuery( nextWd[0], prop )
                    else:
                    
                        if len( tag ) == 4:
                        
                            query = propOfQuery( prop, singular( tag[idxKey][0] ) )

        else:

            idxKey = idxKey + 1
            #print( "outer loop. Looking for next keyword: " )
            idxKey = nextKeyword( tag, idxKey )
            query = handleKeyword( tag, idxKey, countExist )
                
    else:

        query = handleKeyword( tag, idxKey, countExist )
        
    #print( query )
            
    return query

def handleKeyword( tag, idxKey, countExist ):

    keyword = tag[idxKey][0]
    keyTag = tag[idxKey][1]
    queryPart = ""
    #bunch of ifs yo
    count = 1
    if keyword == "starting":
        
        prevWd = tag[idxKey - 1]
        nextWd = tag[idxKey + count]
        #if before starting is a noun, keep going
        if prevWd[1] == "NNS" or prevWd[1] == "NNPS":

            if nextWd[0] == "with":

                count = count + 1

                if countExist == 1:

                    if tag[idxKey + count][1] != "CD":
                        
                        queryPart = startWithQuery( singular( prevWd[0] ), tag[idxKey + count][0], 1)
                else:
                    
                    if tag[idxKey + count][1] != "CD":
                        
                        queryPart = startWithQuery( singular( prevWd[0] ), tag[idxKey + count][0], 0 )
                    
    elif keyword == "ending":

        prevWd = tag[idxKey - 1]
        nextWd = tag[idxKey + count]
        if prevWd[1] == "NNS" or prevWd[1] == "NNPS":

            if nextWd[0] == "with":

                count = count + 1

                if countExist == 1:
                    
                    if tag[idxKey + count][1] != "CD":
                        
                        queryPart = endWithQuery( singular( prevWd[0] ), tag[idxKey + count][0], 1 )
                else:

                    if tag[idxKey + count][1] != "CD":
                        
                        queryPart = endWithQuery( singular( prevWd[0] ), tag[idxKey + count][0], 0 )
               
    elif keyword == "containing":

        prevWd = tag[idxKey - 1]
        if prevWd[1] == "NNS" or prevWd[1] == "NNPS":
            
            if countExist == 1:
                
                if tag[idxKey + count][1] != "CD":
                        
                    queryPart = containQuery( singular( prevWd[0] ), tag[idxKey + count][0], 1 )
                
            else:

                if tag[idxKey + count][1] != "CD":
                
                    queryPart = containQuery( singular( prevWd[0] ), tag[idxKey + count][0], 0 )
                
    elif keyword == "greater":

        prevWd = tag[idxKey - 1]
        nextWd = tag[idxKey + count]

        #check if than is next
        if nextWd[0] == "than":
            
            count = count + 1
            nextWd = tag[idxKey + count]

            #if next tag after than is a quantity then we matched a relation
            if nextWd[1] == "CD":

                if countExist == 1:

                    queryPart = equalityQuery( singular( prevWd[0] ), singular( prevWd[0] ), tag[idxKey + count][0], ">", 1 )
                    
                else:
                    
                    queryPart = equalityQuery( singular( prevWd[0] ), singular( prevWd[0] ), tag[idxKey + count][0], ">", 0 )
            #if its or instead, then it could be "or equal to"    
            elif nextWd[0] == "or":
                
                count = count + 1
                nextWd = tag[idxKey + count]
                
                if nextWd[0] == "equal":

                    while nextWd[1] != "CD":
                        
                        count = count + 1
                        nextWd = tag[idxKey + count]

                    if countExist == 1:

                        queryPart = equalityQuery( singular( prevWd[0] ), singular( prevWd[0] ), tag[idxKey + count][0], ">=", 1 )
                        
                    else:
                        
                        queryPart = equalityQuery( singular( prevWd[0] ), singular( prevWd[0] ), tag[idxKey + count][0], ">=", 0 )


    elif keyword == "less":

        prevWd = tag[idxKey - 1]
        nextWd = tag[idxKey + count]
        
        if nextWd[0] == "than":
            
            count = count + 1
            nextWd = tag[idxKey + count]
            
            if nextWd[1] == "CD":

                if countExist == 1:

                    queryPart = equalityQuery( singular( prevWd[0] ), singular( prevWd[0] ), tag[idxKey + count][0], "<", 1 )

                else:
                
                    queryPart = equalityQuery( singular( prevWd[0] ), singular( prevWd[0] ), tag[idxKey + count][0], "<", 0 )
                
            elif nextWd[0] == "or":
                
                count = count + 1
                nextWd = tag[idxKey + count]
                
                if nextWd[0] == "equal":

                    while nextWd[1] != "CD":
                        
                        count = count + 1
                        nextWd = tag[idxKey + count]

                    if countExist == 1:

                        queryPart = equalityQuery( singular( prevWd[0] ), singular( prevWd[0] ), tag[idxKey + count][0], "<=", 1 )
                        
                    else:
                        
                        queryPart = equalityQuery( singular( prevWd[0] ), singular( prevWd[0] ), tag[idxKey + count][0], "<=", 0 )


    elif keyword == "equal":
        
        beforeEqual = tag[idxKey -1]
        isNot = 0
        
        if beforeEqual[0] == "not":
            
            prevWd = tag[idxKey - 2]
            isNot = 1

        else:

            prevWd = tag[idxKey - 1]
            
        nextWd = tag[idxKey + count]
        
        while nextWd[1] != "CD":

            count = count + 1
            nextWd = tag[idxKey + count]

        
        if isNot == 1:

            if countExist == 1:

                queryPart = equalityQuery( singular( prevWd[0] ), singular( prevWd[0] ), tag[idxKey + count][0], "<>", 1 )
                
            else:
                
                queryPart = equalityQuery( singular( prevWd[0] ), singular( prevWd[0] ), tag[idxKey + count][0], "<>", 0 )
            
        else:

            if countExist == 1:

                 queryPart = equalityQuery( singular( prevWd[0] ), singular( prevWd[0] ), tag[idxKey + count][0], "=", 1 )
                
            else:
                
                 queryPart = equalityQuery( singular( prevWd[0] ), singular( prevWd[0] ), tag[idxKey + count][0], "=", 0 )
        
    elif keyword == "where":

        nextWd = tag[idxKey + count]
        prop2 = singular( tag[idxKey - 1][0] )
        #Added to detect templates with where
        if nextWd[1] == "NN" or nextWd[1] == "NNP" or nextWd[1] == "NNS" or nextWd[1] == "NNPS":
            
            prevWd = tag[idxKey - 1]
            currWd = nextWd
            count = count + 1

            if tag[idxKey + count][0] == "starts" or tag[idxKey + count][0] == "start":
                
                count = count + 1
                nextWd = tag[idxKey + count]
                
                if nextWd[0] == "with":
                    
                    count = count + 1
                    
                if countExist == 1:

                    if tag[idxKey + count][1] != "CD":
                        
                        queryPart = startWithQuery( singular( currWd[0] ), tag[idxKey + count][0], 1 )
                    
                else:
                    if tag[idxKey + count][1] != "CD":
                        
                        queryPart = startWithQuery( singular( currWd[0] ), tag[idxKey + count][0], 0 )
                    
            elif tag[idxKey + count][0] == "ends" or tag[idxKey + count][0] == "end":
                
                count = count + 1
                nextWd = tag[idxKey + count]

                if nextWd[0] == "with":
                    
                    count = count + 1
                    
                    if countExist == 1:

                        if tag[idxKey + count][1] != "CD":
                            
                            queryPart = endWithQuery( singular( currWd[0] ), tag[idxKey + count][0], 1 )
                        
                    else:
                        if tag[idxKey + count][1] != "CD":
                            
                            queryPart = endWithQuery( singular( currWd[0] ), tag[idxKey + count][0], 0 )
                    
            elif tag[idxKey + count][0] == "contains" or tag[idxKey + count][0] == "contain":
                
                count = count + 1
                
                if countExist == 1:
                    
                    if tag[idxKey + count][1] != "CD":
                        
                        queryPart = containQuery( singular( currWd[0] ), tag[idxKey + count][0], 1 )
                                              
                else:
                    if tag[idxKey + count][1] != "CD":
                        
                        queryPart = containQuery( singular( currWd[0] ), tag[idxKey + count][0], 0 )
                                              
            elif tag[idxKey + count][0] == "is" or tag[idxKey + count][0] == "are":

                count = count + 1
                prop = tag[idxKey + 1]
                nextWd = tag[idxKey + count]

                if nextWd[1] == "JJ" and ( nextWd[0] != "greater" and nextWd[0] != "less" and nextWd[0] != "equal" and nextWd[0] != "null" ):

                    queryPart = "MATCH (n {" + prop[0] + " : '" + nextWd[0] + "'})" + "\n" + "RETURN n"
                    
                elif nextWd[0] == "greater":

                    count = count + 1
                    prevWd = tag[idxKey - 1]
                    nextWd = tag[idxKey + count]
                    
                    if nextWd[0] == "than":
                        
                        count = count + 1
                        nextWd = tag[idxKey + count]
                        
                        if nextWd[1] == "CD":

                            if countExist == 1:

                                queryPart = equalityQuery( singular( currWd[0] ), prop2, tag[idxKey + count][0], ">", 1 )
                                
                            else:
                            
                                queryPart = equalityQuery( singular( currWd[0] ), prop2, tag[idxKey + count][0], ">", 0 )
                            
                        elif nextWd[0] == "or":
                            
                            count = count + 1
                            nextWd = tag[idxKey + count]
                            
                            if nextWd[0] == "equal":

                                while nextWd[1] != "CD":
                                    
                                    count = count + 1
                                    nextWd = tag[idxKey + count]
                                    
                                if countExist == 1:

                                     queryPart = equalityQuery( singular( currWd[0] ), prop2, tag[idxKey + count][0], ">=", 1 )

                                else:
                                
                                     queryPart = equalityQuery( singular( currWd[0] ), prop2, tag[idxKey + count][0], ">=", 0 )

                elif nextWd[0] == "less":

                    count = count + 1
                    prevWd = tag[idxKey - 1]
                    nextWd = tag[idxKey + count]
                    
                    if nextWd[0] == "than":
                        
                        count = count + 1
                        nextWd = tag[idxKey + count]
                        
                        if nextWd[1] == "CD":

                            if countExist == 1:

                                queryPart = equalityQuery( singular( currWd[0] ), prop2, tag[idxKey + count][0], "<", 1 )

                            else:
                            
                                queryPart = equalityQuery( singular( currWd[0] ), prop2, tag[idxKey + count][0], "<", 0 )
                            
                        elif nextWd[0] == "or":
                            
                            count = count + 1
                            nextWd = tag[idxKey + count]
                            
                            if nextWd[0] == "equal":

                                while nextWd[1] != "CD":
                                    
                                    count = count + 1
                                    nextWd = tag[idxKey + count]
                                    
                                if countExist == 1:

                                    queryPart = equalityQuery( singular( currWd[0] ), prop2, tag[idxKey + count][0], "<=", 1 )
                                    
                                else:
                                
                                    queryPart = equalityQuery( singular( currWd[0] ), prop2, tag[idxKey + count][0], "<=", 0 )


                elif nextWd[0] == "equal":
                    
                    while nextWd[1] != "CD":

                        count = count + 1
                        nextWd = tag[idxKey + count]

                    if countExist == 1:
                            
                        queryPart = equalityQuery( singular( currWd[0] ), prop2, tag[idxKey + count][0], "=", 1 )
                            
                    else:
                            
                        queryPart = equalityQuery( singular( currWd[0] ), prop2, tag[idxKey + count][0], "=", 0 )
                        
                elif nextWd[0] == "not":

                    count = count + 1
                    nextWd = tag[idxKey + count]
                    
                    if nextWd[0] == "equal":
                        
                        while nextWd[1] != "CD":
                            
                            count = count + 1
                            nextWd = tag[idxKey + count]
                                        
                        if countExist == 1:
                            
                            queryPart = equalityQuery( singular( currWd[0] ), prop2, tag[idxKey + count][0], "<>", 1 )
                            
                        else:
                            
                            queryPart = equalityQuery( singular( currWd[0] ), prop2, tag[idxKey + count][0], "<>", 0 )
                    
                    elif nextWd[0] == "null":

                        if countExist == 1:

                            queryPart = nullPropQuery( singular( currWd[0] ), 0, 1 )

                        else:
                            
                            queryPart = nullPropQuery( singular( currWd[0] ), 0, 0 )

                elif nextWd[0] == "null":

                        if countExist == 1:

                            queryPart = nullPropQuery( singular( currWd[0] ), 1, 1 )
                            
                        else:
                            
                            queryPart = nullPropQuery( singular( currWd[0] ), 1, 0 )
                                        
    elif keyword == "and":

        prop = ""

        #Search for first noun
        for i in range( 0, len( tag ) ):

            if tag[i][1] == "NNS" or tag[i][1] == "NNPS":

                prop = singular( tag[i][0] )
                break
            
        var = prop[0]

        #Nouns before and after "and"
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
        queryPart = "MATCH (" + var + " :" + queryPart + ")" + "\n" + "RETURN " + var + "." + prop

    elif keyTag == "NNPS" or keyTag == "NNS":

        #Could not find keywords.. oh oh
        queryPart = singular( tag[idxKey][0] )
        
    return queryPart

#tag = getInput()
#parse( tag )

