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

print( tag )

query = ""


#Right now, check if first word is our keyword get
if tag[0][0] == "get":

    nTag = tag[1][1]


    #Need to implement if they use words like all
    if tag[1][0] == "DT":

        print( "determinant" )
        
    #if not, we can check if they are trying to get a plural noun
    elif nTag == "NNS" or nTag == "NNPS":

        #print( "noun plural" )
        label = tag[1][0]

        #If it is a plural noun, and thats all there is to the string
        #Then its match label
        if len( tag ) == 2:

            var = tag[1][0][0]
            #print( var )

            query = "Match(" + var + " :" + label + ")" + "\n" + "RETURN " + var

        else:
        
            nTag = tag[2][1]

            #If third word is tagged in, perhaps its a property????
            if nTag == "IN":

                var = tag[1][0][0]
                prop = lem.lemmatize( tag[1][0] )
                nTag = tag[3][1]

                #If fourth word is noun, then its match property of label
                if nTag == "NNS" or nTag == "NNPS":

                    label = lem.lemmatize( tag[3][0] )
                    label = label[0].upper() + label[1:]

                    #Nothing else
                    if len( tag ) == 4:
   
                        query = "Match(" + var + " :" + label + ")" + "\n" + "RETURN " + var + "." + prop
            
        
print( query )
            


