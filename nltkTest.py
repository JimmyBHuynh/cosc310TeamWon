import nltk
from nltk.corpus import treebank #Inflect engine faster than lemmatizer for singularizing words
#import inflect
from nltk.stem import WordNetLemmatizer

#Lemmatizer
lem = WordNetLemmatizer()

#Inflect engine
#engine = inflect.engine()

keywords = "get", "count", "number", "of", "where"


#Get input --> Going to be function in itself later
    
phrase = input( "Query: " )
tokens = nltk.word_tokenize( phrase.lower() )

tag = nltk.pos_tag( tokens )

iterTag = iter( tag )

print( tag )

query = ""

count = 0
#Needto: add a while( next(iterTag)[0] != "get" before here

while next( iterTag )[ 0 ] != "get":

    count = count + 1


#Right now, check if first word is our keyword get
count = count + 1
nTag = next( iterTag, None )

#print( str( count ) )
#print( len( tag ) )

    #Need to implement if they use words like all
if nTag[1] == "DT":

    print( "determinant" )
        
#if not, we can check if they are trying to get a plural noun

    #Sometimes a word is put after Get that is not a noun.
    #Need to handle that case before here


elif nTag[1] == "NNS" or nTag[1] == "NNPS":

    #print( "noun plural" )
    label = lem.lemmatize( nTag[0] )
    count = count + 1

    #If it is a plural noun, and thats all there is to the string
    #Then its match label
    if len( tag ) == count:

        var = nTag[0][0]
        #print( var )

        query = "Match(" + var + " :" + label + ")" + "\n" + "RETURN " + var

    else:

        #ADD WHILE LOOP HERE LOOKING FOR MORE KEYWORDS - NUMBER OF, COUNT OF
        """

        dictionary.contains( currWord )?
        if contains ---- check tag of currWord
        do as required for tag


        AFTER YOU MATCH GET, CHECK NEXT WORD!

        To look for: count of, number of, of, where, starts with, ends with, contains
            is null
            is not null
            distinct

            ?? PARENTS OF??? <--- will get matched as a property with current implementation

            Get (prop)___ where name is Joe and is a (label)______ of? 


        """
        nTag = next( iterTag )
        count = count + 1
        #If third word is tagged in, perhaps its a property????
        if nTag[1] == "IN":

            var = tag[count][0][0]
            #PLURALS SOMETIMES DONT WORK --- NOTE WORDS ENDING IN "IES"
            prop = lem.lemmatize( tag[count-2][0] )
            nTag = next( iterTag, None )
            count = count + 1

            #If fourth word is noun, then its match property of label
            if nTag[1] == "NNS" or nTag[1] == "NNPS":

               label = lem.lemmatize( tag[count-1][0] )
               label = label[0].upper() + label[1:]

               #Nothing else
            if len( tag ) == count:
   
                    query = "Match(" + var + " :" + label + ")" + "\n" + "RETURN " + var + "." + prop
            
        
print( query )
            


