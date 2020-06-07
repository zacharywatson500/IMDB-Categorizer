import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import torch  
import spacy 
import sys

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")  

funny_adjectives = ["funny","silly","hilarious","clever","comical","comedic","absurd","ridiculous", "silly", "fun"] 
sad_adjectives = ["touching", "moving", "emotional", "sad", "passionate","moving", "sensitive", "sentimental", "cute", "deep" ]
action_adjectives = ["action","intense","cool","sharp", "tight", "explosive", "violent", "vivid", "cut", "coordinated"] 
scary_adjectives = ["scary", "bloody","chilling","creepy", "gorey", "eerie", "horrifying", "dark", "ominous", "haunting"]


row = 500
file = "IMDB Dataset.xlsx"
data = pd.read_excel(file) #reading fil

if data["sentiment"][row] != "positive": 
	print("Only checks positives, ending program")  
	sys.exit()




data = data["review"][row]
if len(data) >= 10000:
	data = data[:9999] 
data = nlp(data)

funny_counter = 0
sad_counter = 0
action_counter = 0
scary_counter = 0

for token in data: 
	if token.pos_ == 'ADJ': 
		for word in funny_adjectives: 
			if word == token.text: 
				funny_counter += 1 
				break 
		for word in sad_adjectives: 
			if word == token.text: 
				sad_counter += 1 
				break  
		for word in action_adjectives: 
			if word == token.text: 
				action_counter += 1 
				break  
		for word in scary_adjectives: 
			if word == token.text: 
				scary_counter += 1 
				break 



total_counter = funny_counter + sad_counter + action_counter + scary_counter 


