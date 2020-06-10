import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import torch  
import spacy 
import nltk
from nltk.corpus import wordnet as wn
import sys 

def set_underscore_remover(set_input): 
	
	for word in set_input.copy(): 
		if '_' in word or '-' in word: 
			set_input.remove(str(word)) 
	return set_input

#spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")    

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


print('Funny: ',funny_synonyms)
print('Sad: ',sad_synonyms)
print('Action: ',action_synonyms)
print('Scary: ',scary_synonyms) 

# funny_adjectives = ["funny","silly","hilarious","clever","comical","comedic","absurd","ridiculous", "silly", "fun"] 
# sad_adjectives = ["touching", "moving", "emotional", "sad", "passionate","moving", "sensitive", "sentimental", "cute", "deep" ]
# action_adjectives = ["action","intense","cool","sharp", "tight", "explosive", "violent", "vivid", "cut", "coordinated"] 
# scary_adjectives = ["scary", "bloody","chilling","creepy", "gorey", "eerie", "horrifying", "dark", "ominous", "haunting"]


# row = 500
# file = "IMDB Dataset.xlsx"
# data = pd.read_excel(file) #reading fil

# if data["sentiment"][row] != "positive": 
# 	print("Only checks positives, ending program")  
# 	sys.exit()




# data = data["review"][row]
# if len(data) >= 10000:
# 	data = data[:9999] 
# data = nlp(data)

# funny_counter = 0
# sad_counter = 0
# action_counter = 0
# scary_counter = 0

# for token in data: 
# 	if token.pos_ == 'ADJ': 
# 		for word in funny_adjectives: 
# 			if word == token.text: 
# 				funny_counter += 1 
# 				break 
# 		for word in sad_adjectives: 
# 			if word == token.text: 
# 				sad_counter += 1 
# 				break  
# 		for word in action_adjectives: 
# 			if word == token.text: 
# 				action_counter += 1 
# 				break  
# 		for word in scary_adjectives: 
# 			if word == token.text: 
# 				scary_counter += 1 
# 				break 



# total_counter = funny_counter + sad_counter + action_counter + scary_counter 