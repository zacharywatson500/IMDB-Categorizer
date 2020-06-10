import nltk
from nltk.corpus import wordnet as wn  

def set_underscore_remover(set_input): 
	
	for word in set_input.copy(): 
		if '_' in word or '-' in word: 
			set_input.remove(str(word)) 
	return set_input

funny_synonyms = set() 
sad_synonyms = set() 
action_synonyms = set() 
scary_synonyms = set() 

for synonym in wn.synsets('funny'): 
	for word in synonym.lemma_names(): 
		funny_synonyms.add(str(word))  

for synonym in wn.synsets('hilarious'): 
	for word in synonym.lemma_names(): 
		funny_synonyms.add(str(word)) 

for synonym in wn.synsets('sad'): 
	for word in synonym.lemma_names(): 
		sad_synonyms.add(str(word))  

for synonym in wn.synsets('melancholy'): 
	for word in synonym.lemma_names(): 
		sad_synonyms.add(str(word)) 

for synonym in wn.synsets('sentimental'): 
	for word in synonym.lemma_names(): 
		sad_synonyms.add(str(word)) 

for synonym in wn.synsets('violent'): 
	for word in synonym.lemma_names(): 
		action_synonyms.add(str(word))

for synonym in wn.synsets('exciting'): 
	for word in synonym.lemma_names(): 
		action_synonyms.add(str(word)) 

for synonym in wn.synsets('scary'): 
	for word in synonym.lemma_names(): 
		scary_synonyms.add(str(word))

for synonym in wn.synsets('haunting'): 
	for word in synonym.lemma_names(): 
		scary_synonyms.add(str(word)) 

for synonym in wn.synsets('creepy'): 
	for word in synonym.lemma_names(): 
		scary_synonyms.add(str(word))

for synonym in wn.synsets('ominous'): 
	for word in synonym.lemma_names(): 
		scary_synonyms.add(str(word))

set_underscore_remover(funny_synonyms)
set_underscore_remover(sad_synonyms)
set_underscore_remover(action_synonyms)
set_underscore_remover(scary_synonyms)