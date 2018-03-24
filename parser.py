import nltk
from nltk.corpus import treebank 
#Inflect engine faster than lemmatizer for singularizing words
#Depluralizing has issues with words ending in 'ies' - eg. species/specie
#import inflect
from nltk.stem import WordNetLemmatizer

#Lemmatizer
lem = WordNetLemmatizer()
keywords = "get", "number", "where", "and", "is", "and", "starting", "ending", "containing", "greater", "less", "equal"
query = ""

def init(input):
    
    phrase = input
    tokens = nltk.word_tokenize( phrase.lower() )
    
    tag = nltk.pos_tag( tokens )

    iterTag = iter( tag )

    #print( tag )

    query = ""
    count = 0
	
    results = query3(tag)
	
    if(results == 'No match'):
    	return parse(tag)
    else:
    	return results
    

def getInput():
    
    #Get input --> Going to be function in itself later
        
    phrase = input( "Query: " )
    tokens = nltk.word_tokenize( phrase.lower() )
    
    tag = nltk.pos_tag( tokens )

    iterTag = iter( tag )

    #print( tag )

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

    #print( "First keyword: " + str( tag[count][0] ) )
           
    return count

def nextKeyword( tag, idxKey ):

    while tag[idxKey][0] not in keywords and idxKey < len( tag )-1:

        idxKey = idxKey + 1

    #print( "Next Keyword: " + tag[idxKey][0] )

    return idxKey

def query3Translate(prop, val):
    cypher = "MATCH (n) WHERE n." + prop + " = ‘" + val + "’ RETURN n"
    return cypher;

def query3(tag):
	
	results = ""

	#List of valid non-verb starting words for this query
	startingWord = 'what', 'find', 'get', 'return', 'which', 'match'
	
	#List of words that are 'have' or can be used in place of 'have'
	haveSyn = 'have', 'has', 'possess', 'possesses', 'are' 

	pointer = 0
	length = len(tag)
	
	if pointer == length:
		results = 'No Match'
		return results;

	#currentTag points to a word and token in user query, which are both stored in their sepearte variables
	
	currentTag = tag[pointer]
	currentWord = currentTag[0]
	currentToken = currentTag[1]

	#Method immidiately stops if the starting word isn't in the startingWord list
	if currentWord in startingWord:
		
		
		startingToken = currentToken
		if currentWord == 'what' or currentWord == 'which':
			startingToken = 'WP'
		
		pointer += 1
		
		if pointer == length:
			results = 'No match'
			return results;
			
		currentTag = tag[pointer]
		currentWord = currentTag[0]
		currentToken = currentTag[1]
		
		
		#Check to see if second word is all. If it is, and the first word was a "wh" pronoun, there was a gramatical error. If the first word was not one of those pronouns,
		#the program skips to the next word
		if currentWord == 'all':
			if startingToken == 'WP':
				results = 'No match'
				return results;
			else:
				pointer += 1
				
				if pointer == length:
					results = 'No match'
					return results;
					
				currentTag = tag[pointer]
				currentWord = currentTag[0]
				currentToken = currentTag[1]
		
		#Current word should be a plural noun if using this query type, refering to the nodes (ex: nodes, entries, ect.)
		if currentToken != 'NNS' and currentToken != 'VBZ':
			results = 'No match'
			return results;
		
		pointer += 1
		
		if pointer == length:
			results = 'No match'
			return results;
			
		currentTag = tag[pointer]
		currentWord = currentTag[0]
		currentToken = currentTag[1]
		
		#If starting word was not a wh pronoun, current word could be a wh pronoun or 'that'. If it is, it is 'prev' is set to true, then the word is iterated over.
		prev = False
		if startingToken != 'WP':
			if currentWord == 'that' or currentWord == 'who' or currentWord == 'which':
			
				pointer += 1
		
				if pointer == length:
					results = 'No match'
					return results;
				
				prev = True
				currentTag = tag[pointer]
				currentWord = currentTag[0]
				currentToken = currentTag[1]
		
		#Next word can be 'with' if it comes directly after the noun, or part of the haveSyn list if either the starting token was a wh pronoun or the previous token was a wh pronoun or that
		if prev == False and currentToken == 'IN' or prev == True and currentWord in haveSyn or startingToken == 'WP' and currentWord in haveSyn:
			pointer += 1
		
			if pointer == length:
				results = 'No match'
				return results;
				
			currentTag = tag[pointer]
			currentWord = currentTag[0]
			currentToken = currentTag[1]
		else:
			results = 'No match'
			return results;
		
		#User will often put an 'a' for this word. Syntax is valid either way, so it can just be iterated over if it is an 'a'
		if currentWord == 'a' or currentWord == 'an':
			pointer += 1
		
			if pointer == length:
				results = 'No match'
				return results;
				
			currentTag = tag[pointer]
			currentWord = currentTag[0]
			currentToken = currentTag[1]
			
		#If the user has valid syntax there are two scenarios for the remainder of the query
		#1) Two words remain, the first of which is the attribute being searched, the second being the attribute values
		#2) Three words remain, the first being the attribute searched, the second being 'of', the third being the attribute value
		remainingWords = length - pointer
		
		if remainingWords == 2:
			attribute = currentWord
			pointer += 1
			currentTag = tag[pointer]
			value = currentTag[0]
			
			results = attribute, value
			return results;
		
		elif remainingWords == 3:
			attribute = currentWord
			pointer += 1
			currentTag = tag[pointer]
			currentWord = currentTag[0]
			
			if(currentWord != 'of'):
				results = 'No match'
				return results;
				
			pointer += 1
			currentTag = tag[pointer]
			value = currentTag[0]
			
			results = attribute, value
			return results;

		results = 'No match'
		return results;
		
	else:
		results = 'No match'
		return results;
	
def parse( tag ):

    countExist = 0
    distinct = 0
    order = 0

    #check if count exists, then we need to change states
    for i in range( 0, len( tag ) ):

        if tag[i][0] == "count":

            countExist = 1

        if tag[i][0] == "distinct":

            distinct = 1

        if tag[i][0] == "order":

            order = 1
        
        
    idxKey = getFirstKeyword( tag )
    query = ""

    if tag[idxKey + 1][1] == "DT":

        #Determinant handling
        #print( "determinant: " )
        idxKey = idxKey + 1

    elif tag[idxKey + 1][1] == "NNS" or tag[idxKey + 1][1] == "NNPS" or tag[idxKey + 1] == "NN" or tag[idxKey +1] == "NNP":

        #most likely, we found a noun after get
        idxKey = idxKey + 1
        prop = singular( tag[idxKey][0] )
        var = tag[idxKey][0][0]

        #Plural noun handling
        if idxKey + 1 == len( tag ):

            var = tag[idxKey][0][0]
            query = "Match(" + var + " :" + singular( tag[idxKey][0] ) + ")" + "\n" + "RETURN " + var  

        elif tag[idxKey + 1][0] == "that":
            idxKey = idxKey + 1
            nextWd = tag[idxKey + 1]
            if nextWd[0] == "are":
                idxKey = idxKey + 1
                nextWd = tag[idxKey + 1]
                if nextWd[1] == "NNS" or nextWd[1] == "NNPS":

                    if order == 1:

                        lastWd = tag[len( tag )-1]
                        if lastWd[1] == "NN" or lastWd[1] == "NNP":

                            query = "MATCH () -[:" + nextWd[0] + "] -> (n)" + "\n" + "RETURN n." + prop + " ORDER BY n." + lastWd[0]
                        
                    else:
                        
                        query = "MATCH () -[:" + nextWd[0] + "] -> (n)" + "\n" + "RETURN n." + prop
  
        else:

            #Dunno, let's look for next keyword
            #print( "looking for next keyword" )
            idxKey = nextKeyword( tag, idxKey )

            if tag[idxKey][0] not in keywords:

                #This is how you get names of persons
                if len( tag ) == 4:
                    
                    query = "MATCH(" + var + " :" + singular( tag[idxKey][0] ) + ")" + "\n" + "RETURN " + var + "." + prop

                else:

                    idxKey = 1
                    
                    while tag[idxKey][0] != "that":
                        
                        idxKey = idxKey + 1
                    #print( tag[idxKey][0] )
                
            else:

                #other wise
                query = handleKeyword( tag, idxKey, countExist )

    else:

        idxKey = idxKey + 1
        #print( "outer loop. Looking for next keyword: " )
        idxKey = nextKeyword( tag, idxKey )
        query = handleKeyword( tag, idxKey, countExist )
            
    
    #print(query) 
    # return   
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

                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " STARTS WITH " + "\"" + tag[idxKey + count][0] + "\"\n" + "RETURN COUNT (n." + singular( prevWd[0] ) + ")"

                else:

                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " STARTS WITH " + "\"" + tag[idxKey + count][0] + "\"\n" + "RETURN n." + singular( prevWd[0] )

    elif keyword == "ending":

        prevWd = tag[idxKey - 1]
        nextWd = tag[idxKey + count]
        if prevWd[1] == "NNS" or prevWd[1] == "NNPS":

            if nextWd[0] == "with":

                count = count + 1

                if countExist == 1:
                    
                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " ENDS WITH " + "\"" + tag[idxKey + count][0] +"\"\n" + "RETURN COUNT (n." + singular( prevWd[0] ) + ")"

                else:

                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " ENDS WITH " + "\"" + tag[idxKey + count][0] +"\"\n" + "RETURN n." + singular( prevWd[0] )
 
    elif keyword == "containing":

        prevWd = tag[idxKey - 1]
        if prevWd[1] == "NNS" or prevWd[1] == "NNPS":
            
            if countExist == 1:
                
                queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " CONTAINS " + "\"" + tag[idxKey + count][0] +"\"\n" + "RETURN COUNT (n." + singular( prevWd[0] ) + ")"

            else:
                
                queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " CONTAINS " + "\"" + tag[idxKey + count][0] +"\"\n" + "RETURN n." + singular( prevWd[0] )
                
    elif keyword == "greater":

        prevWd = tag[idxKey - 1]
        nextWd = tag[idxKey + count]
        
        if nextWd[0] == "than":
            
            count = count + 1
            nextWd = tag[idxKey + count]
            
            if nextWd[1] == "CD":

                if countExist == 1:

                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " > " + tag[idxKey + count][0] + "\n" + "RETURN COUNT (n." + singular( prevWd[0] ) + ")"                

                else:
                    
                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " > " + tag[idxKey + count][0] + "\n" + "RETURN n." + singular( prevWd[0] )
                
            elif nextWd[0] == "or":
                
                count = count + 1
                nextWd = tag[idxKey + count]
                
                if nextWd[0] == "equal":

                    while nextWd[1] != "CD":
                        
                        count = count + 1
                        nextWd = tag[idxKey + count]

                    if countExist == 1:

                        queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " >= " + tag[idxKey + count][0] + "\n" + "RETURN COUNT (n." + singular( prevWd[0] ) + ")"           
                        
                    else:
                        
                        queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " >= " + tag[idxKey + count][0] + "\n" + "RETURN n." + singular( prevWd[0] )


    elif keyword == "less":

        prevWd = tag[idxKey - 1]
        nextWd = tag[idxKey + count]
        
        if nextWd[0] == "than":
            
            count = count + 1
            nextWd = tag[idxKey + count]
            
            if nextWd[1] == "CD":

                if countExist == 1:

                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " < " + tag[idxKey + count][0] + "\n" + "RETURN COUNT (n." + singular( prevWd[0] ) + ")"           

                else:
                
                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " < " + tag[idxKey + count][0] + "\n" + "RETURN n." + singular( prevWd[0] )
                
            elif nextWd[0] == "or":
                
                count = count + 1
                nextWd = tag[idxKey + count]
                
                if nextWd[0] == "equal":

                    while nextWd[1] != "CD":
                        
                        count = count + 1
                        nextWd = tag[idxKey + count]

                    if countExist == 1:

                        queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " <= " + tag[idxKey + count][0] + "\n" + "RETURN COUNT (n." + singular( prevWd[0] ) + ")"               
                        
                    else:
                        
                        queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " <= " + tag[idxKey + count][0] + "\n" + "RETURN n." + singular( prevWd[0] )


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

                queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " <> " + tag[idxKey + count][0] + "\n" + "RETURN COUNT (n." + singular( prevWd[0] ) + ")"             
                
            else:
                
                queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " <> " + tag[idxKey + count][0] + "\n" + "RETURN n." + singular( prevWd[0] )
            
        else:

            if countExist == 1:

                 queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " = " + tag[idxKey + count][0] + "\n" + "RETURN COUNT (n." + singular( prevWd[0] ) + ")"      
                
            else:
                
                queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( prevWd[0] ) + " = " + tag[idxKey + count][0] + "\n" + "RETURN n." + singular( prevWd[0] )
        
    elif keyword == "where":

        nextWd = tag[idxKey + count]
        if nextWd[1] == "NN" or nextWd[1] == "NNP" or nextWd[1] == "NNS" or nextWd[1] == "NNPS":
            
            prevWd = tag[idxKey - 1]
            currWd = nextWd
            count = count + 1

            if tag[idxKey + count][0] == "starts":
                
                count = count + 1
                nextWd = tag[idxKey + count]
                
                if nextWd[0] == "with":
                    
                    count = count + 1
                    
                if countExist == 1:
                    
                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " STARTS WITH " + "\"" + tag[idxKey + count][0] + "\"\n" + "RETURN COUNT (n." + singular( currWd[0] ) + ")"

                else:
                    
                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " STARTS WITH " + "\"" + tag[idxKey + count][0] + "\"\n" + "RETURN n." + singular( currWd[0] )
                    
            elif tag[idxKey + count][0] == "ends":
                
                count = count + 1
                nextWd = tag[idxKey + count]

                if nextWd[0] == "with":
                    
                    count = count + 1
                    
                    if countExist == 1:
                        
                        queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " ENDS WITH " + "\"" + tag[idxKey + count][0] +"\"\n" + "RETURN COUNT (n." + singular( currWd[0] ) + ")"

                    else:
                        
                        queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " ENDS WITH " + "\"" + tag[idxKey + count][0] +"\"\n" + "RETURN n." + singular( currWd[0] )                   
                
            elif tag[idxKey + count][0] == "contains":
                
                count = count + 1
                
                if countExist == 1:
                    
                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " CONTAINS " + "\"" + tag[idxKey + count][0] +"\"\n" + "RETURN COUNT (n." + singular( currWd[0] ) + ")"

                else:
                    
                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " CONTAINS " + "\"" + tag[idxKey + count][0] +"\"\n" + "RETURN n." + singular( currWd[0] )
            
            if tag[idxKey + count][0] == "is":

                count = count + 1
                prop = tag[idxKey + 1]
                nextWd = tag[idxKey + count]

                if nextWd[1] == "JJ" and ( nextWd[0] != "greater" and nextWd[0] != "less" and nextWd[0] != "equal" and nextWd[0] != "null" ):

                    queryPart = "Match (n {" + prop[0] + " : '" + nextWd[0] + "'})" + "\n" + "RETURN n"
                    
                elif nextWd[0] == "greater":

                    count = count + 1
                    prevWd = tag[idxKey - 1]
                    nextWd = tag[idxKey + count]
                    
                    if nextWd[0] == "than":
                        
                        count = count + 1
                        nextWd = tag[idxKey + count]
                        
                        if nextWd[1] == "CD":

                            if countExist == 1:

                                queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " > " + tag[idxKey + count][0] + "\n" + "RETURN COUNT (n." + singular( currWd[0] ) + ")"

                            else:
                            
                                queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " > " + tag[idxKey + count][0] + "\n" + "RETURN n." + singular( currWd[0] )
                            
                        elif nextWd[0] == "or":
                            
                            count = count + 1
                            nextWd = tag[idxKey + count]
                            
                            if nextWd[0] == "equal":

                                while nextWd[1] != "CD":
                                    
                                    count = count + 1
                                    nextWd = tag[idxKey + count]
                                    
                                if countExist == 1:

                                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " >= " + tag[idxKey + count][0] + "\n" + "RETURN COUNT (n." + singular( currWd[0] ) + ")"

                                else:
                                
                                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " >= " + tag[idxKey + count][0] + "\n" + "RETURN n." + singular( currWd[0] )  


                elif nextWd[0] == "less":

                    count = count + 1
                    prevWd = tag[idxKey - 1]
                    nextWd = tag[idxKey + count]
                    
                    if nextWd[0] == "than":
                        
                        count = count + 1
                        nextWd = tag[idxKey + count]
                        
                        if nextWd[1] == "CD":

                            if countExist == 1:

                                queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " < " + tag[idxKey + count][0] + "\n" + "RETURN COUNT (n." + singular( currWd[0] ) + ")"

                            else:
                            
                                queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " < " + tag[idxKey + count][0] + "\n" + "RETURN n." + singular( currWd[0] )
                            
                        elif nextWd[0] == "or":
                            
                            count = count + 1
                            nextWd = tag[idxKey + count]
                            
                            if nextWd[0] == "equal":

                                while nextWd[1] != "CD":
                                    
                                    count = count + 1
                                    nextWd = tag[idxKey + count]
                                    
                                if countExist == 1:

                                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " <= " + tag[idxKey + count][0] + "\n" + "RETURN COUNT (n." + singular( currWd[0] ) + ")"

                                else:
                                
                                    queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " <= " + tag[idxKey + count][0] + "\n" + "RETURN n." + singular( currWd[0] )


                elif nextWd[0] == "equal":
                    
                    while nextWd[1] != "CD":

                        count = count + 1
                        nextWd = tag[idxKey + count]

                        if countExist == 1:
                            
                            queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " = " + tag[idxKey + count][0] + "\n" + "RETURN COUNT (n." + singular( currWd[0] ) + ")"                      
                            
                        else:
                            
                            queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " = " + tag[idxKey + count][0] + "\n" + "RETURN n." + singular( currWd[0] )
                        
                elif nextWd[0] == "not":

                    count = count + 1
                    nextWd = tag[idxKey + count]
                    
                    if nextWd[0] == "equal":
                        
                        while nextWd[1] != "CD":
                            
                            count = count + 1
                            nextWd = tag[idxKey + count]
                                        
                        if countExist == 1:
                            
                            queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " <> " + tag[idxKey + count][0] + "\n" + "RETURN COUNT (n." + singular( currWd[0] ) + ")"                      
                            
                        else:
                            
                            queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " <> " + tag[idxKey + count][0] + "\n" + "RETURN n." + singular( currWd[0] )

                    elif nextWd[0] == "null":

                        if countExist == 1:

                            queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " IS NOT NULL" + "\n" + "RETURN COUNT (n." + singular( prevWd[0] ) + ")"

                        else:
                            
                            queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " IS NOT NULL" + "\n" + "RETURN n." + singular( prevWd[0] )

                elif nextWd[0] == "null":

                        if countExist == 1:

                            queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " IS NULL" + "\n" + "RETURN COUNT (n." + singular( prevWd[0] )  + ")"                         
                            
                        else:
                            
                            queryPart = "MATCH (n)" + "\n" + "WHERE n." + singular( currWd[0] ) + " IS NULL" + "\n" + "RETURN n." + singular( prevWd[0] )
                    
                        
                    
    elif keyword == "and":

        prop = ""

        for i in range( 0, len( tag ) ):

            if tag[i][1] == "NNS" or tag[i][1] == "NNPS":

                prop = singular( tag[i][0] )
                break
        var = prop[0]

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
        queryPart = "Match(" + var + " :" + queryPart + ")" + "\n" + "RETURN " + var + "." + prop

    elif keyTag == "NNPS" or keyTag == "NNS":

        #Could not find keywords.. oh oh
        queryPart = singular( tag[idxKey][0] )
        
    return queryPart
