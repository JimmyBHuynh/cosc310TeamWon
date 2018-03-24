from neo4j.v1 import GraphDatabase;
import nltk
from nltk.corpus import treebank
from nltk.stem import WordNetLemmatizer
	
lem = WordNetLemmatizer()

def query3(phrase):
	
	results = ""

	#Use nltk to get word type
	tokens = nltk.word_tokenize( phrase.lower() )

	#List of valid non-verb starting words for this query
	startingWord = 'what', 'find', 'get', 'return', 'which', 'match'
	
	#List of words that are 'have' or can be used in place of 'have'
	haveSyn = 'have', 'has', 'possess', 'possesses', 'are' 

	tag = nltk.pos_tag( tokens )

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
			results = 'No Match B'
			return results;
			
		currentTag = tag[pointer]
		currentWord = currentTag[0]
		currentToken = currentTag[1]
		
		
		#Check to see if second word is all. If it is, and the first word was a "wh" pronoun, there was a gramatical error. If the first word was not one of those pronouns,
		#the program skips to the next word
		if currentWord == 'all':
			if startingToken == 'WP':
				results = 'No match C'
				return results;
			else:
				pointer += 1
				
				if pointer == length:
					results = 'No Match D'
					return results;
					
				currentTag = tag[pointer]
				currentWord = currentTag[0]
				currentToken = currentTag[1]
		
		#Current word should be a plural noun if using this query type, refering to the nodes (ex: nodes, entries, ect.)
		if currentToken != 'NNS' and currentToken != 'VBZ':
			results = 'No match E' + currentToken + currentWord
			return results;
		
		pointer += 1
		
		if pointer == length:
			results = 'No Match F'
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
					results = 'No Match G'
					return results;
				
				prev = True
				currentTag = tag[pointer]
				currentWord = currentTag[0]
				currentToken = currentTag[1]
		
		#Next word can be 'with' if it comes directly after the noun, or part of the haveSyn list if either the starting token was a wh pronoun or the previous token was a wh pronoun or that
		if prev == False and currentToken == 'IN' or prev == True and currentWord in haveSyn or startingToken == 'WP' and currentWord in haveSyn:
			pointer += 1
		
			if pointer == length:
				results = 'No Match H'
				return results;
				
			currentTag = tag[pointer]
			currentWord = currentTag[0]
			currentToken = currentTag[1]
		else:
			results = 'No match I' + currentToken
			return results;
		
		#User will often put an 'a' for this word. Syntax is valid either way, so it can just be iterated over if it is an 'a'
		if currentWord == 'a' or currentWord == 'an':
			pointer += 1
		
			if pointer == length:
				results = 'No Match J'
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
				results = 'No match K'
				return results;
				
			pointer += 1
			currentTag = tag[pointer]
			value = currentTag[0]
			
			results = attribute, value
			return results;

		results = 'No match L'
		return results;
		
	else:
		results = 'No match A'
		return results;

	print( tag )
