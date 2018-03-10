import nltk
from nltk.corpus import treebank
#Inflect engine faster than lemmatizer for singularizing words
#import inflect
from nltk.stem import WordNetLemmatizer

#Lemmatizer
lem = WordNetLemmatizer()

#Inflect engine
#engine = inflect.engine()


#Get input --> Going to be function in itself later
    
phrase = input( "Query: " )
tokens = nltk.word_tokenize( phrase.lower() )

tag = nltk.pos_tag( tokens )

iterTag = iter( tag )

print( tag )

query = ""


#Right now, check if first word is our keyword get
if next( iterTag )[0] == "get":

    nTag = next( iterTag, None )

    #Need to implement if they use words like all
    if nTag[1] == "DT":

        print( "determinant" )
        
    #if not, we can check if they are trying to get a plural noun
    elif nTag[1] == "NNS" or nTag[1] == "NNPS":

        #print( "noun plural" )
        label = nTag[0]

        #If it is a plural noun, and thats all there is to the string
        #Then its match label
        if len( tag ) == 2:

            var = nTag[0][0]
            #print( var )

            query = "Match(" + var + " :" + label + ")" + "\n" + "RETURN " + var

        else:
        
            nTag = next( iterTag )

            #If third word is tagged in, perhaps its a property????
            if nTag[1] == "IN":

                var = tag[1][0][0]
                prop = lem.lemmatize( tag[1][0] )
                nTag = next( iterTag, None )

                #If fourth word is noun, then its match property of label
                if nTag[1] == "NNS" or nTag[1] == "NNPS":

                    label = lem.lemmatize( tag[3][0] )
                    label = label[0].upper() + label[1:]

                    #Nothing else
                    if len( tag ) == 4:
   
                        query = "Match(" + var + " :" + label + ")" + "\n" + "RETURN " + var + "." + prop
            
        
print( query )
            


