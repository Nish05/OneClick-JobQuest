
# coding: utf-8

# In[6]:

import pymongo as mongo
from pymongo import MongoClient
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer


# In[7]:

# Extracting raw resume from mongodb data
con = mongo.MongoClient(host='127.0.0.1', port=3001)
db = con['meteor']
resume_test = db['resume_test']
result = resume_test.find()
preProcessedResume = []
lemma = WordNetLemmatizer() #Lemmatizer in python
ps = PorterStemmer()  #Stemming in python


# In[8]:

def cleanResume(result):
    
    for record in result:
        
        lines = []
        keywords = []
        resumeKeywords = {}
        
        name = record['Name']
        content = record['Content']
        
        content = content.decode("utf-8") #Decoding the content to string from byte
        print('Name', name)
        print('Content',content)
        for line in content.splitlines(): # spliting the lines of the content
            
            currentWords = line.strip()   # Removing extra spaces from the line
            
            currentWords = re.sub("[^a-zA-Z.+]"," ", currentWords) # Removing irrelavant characters from the words 
            
            currentWords = re.sub(' +',' ',currentWords) # Replacing extra spaces with a single space
            
            currentWords = currentWords.lower() # Converting all the characters to lower case
            
            tokens = currentWords.split(' ') #converting the content to tokens

            stop_words = set(stopwords.words("english")) # Filter out any stop words
            tokens = [token for token in tokens if not token in stop_words]
            
            tokens = list(set(tokens)) # Remove duplicate records from the list of tokens
            keywords.extend(tokens)
            
#         print('Name', name, 'Length : ',len(keywords))
        # Store all the tokens in the form of dictionary
        for i in range( 0, len(keywords)):
            keywords[i] = ps.stem(lemma.lemmatize(keywords[i]))
        resumeKeywords = {'Name': name, 'Content':keywords} 
        
        # Collect all the dictionaries into a single list
        preProcessedResume.append(resumeKeywords)   
        
cleanResume(result)      


# In[9]:

# Insert processed resume into mongodb database
def insertInDB_Resume(preProcessedResume):
    con = mongo.MongoClient(host='127.0.0.1', port=3001)
    db = con['meteor']
    cleanResume_stem_test = db['cleanResume_stem_test']
    print(preProcessedResume)
    db.cleanResume_stem_test.insert_many(preProcessedResume)
insertInDB_Resume(preProcessedResume)
    


# In[ ]:



