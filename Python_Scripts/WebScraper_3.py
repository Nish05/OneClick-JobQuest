
# coding: utf-8

# In[1]:

import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
import pymongo as mongo
from pymongo import MongoClient
import pandas as pd
import sys
print(sys.argv)


# In[10]:

URL = "https://www.indeed.com/jobs?q=software+engineer&l=New+York&start=50"
#conducting a request of the stated URL above:
page = requests.get(URL)
#specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
soup = BeautifulSoup(page.text, "html.parser")
#printing soup in a more structured tree format that makes for easier reading
# print(soup.prettify())
print("Completed scraping from website ......")
print("Started Preprocessing .....")
print("Length of arguments is : ", len(sys.argv))


# In[4]:

lemma = WordNetLemmatizer() #Lemmatizer in python
ps = PorterStemmer()  #Stemming in python

# List for storing the preprocessed job postings
preProcessedPostings = []
def extract_links_from_result(): 
    baseLink = 'https://indeed.com'
    job_post = []
    job_description = []
    job_description_unclean = []
    companies = []
    columns = ["Company-Name","Title","Description"]
    city_set = ["New+York","Chicago","San+Francisco"]
    max_results = 50
    for city in city_set:
        links =[]
        for start in range(0, max_results, 20):  
            page = requests.get("http://www.indeed.com/jobs?q=software+engineer&l=" + str(city) + "&start=" + str(start))
            time.sleep(1)  #ensuring at least 1 second between page grabs
            soup = BeautifulSoup(page.text, "html.parser")
            for div in soup.find_all(name="div", attrs={"class":" row result"}): 
                #grabbing company name
                company = div.find_all(name="span", attrs={"class":"company"}) 
                if len(company) > 0: 
                    for b in company:
                        companies.append(b.text.strip()) 
                else: 
                    sec_try = div.find_all(name="span", attrs={"class":"result-link-source"})
                    for span in sec_try:
                        companies.append(span.text) 
                for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
                    links.append(baseLink+a['href'])
                    job_post.append(a["title"])

            index = 0
            for link in links:
                try:
                    page = requests.get(link)
                except:
                    return

                soup = BeautifulSoup(page.text,'html.parser')
                for script in soup(['script','style']):
                    script.extract()
                text = soup.get_text()
                lines = (line.strip() for line in text.splitlines())  #  Breaking the webpage content into lines
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

                def chunk_space(chunk):
                    chunk_out = chunk + ' ' # Need to fix spacing issue
                    return chunk_out  


                text = ''.join(chunk_space(chunk) for chunk in chunks if chunk).encode('utf-8') # Get rid of all blank lines and ends of line
                 # Now clean out all of the unicode junk (this line works great!!!)
                try:
                    text = text.decode('unicode-escape').encode('ascii', 'ignore') # Need this as some websites aren't formatted
                except:                                                            # in a way that this works, can occasionally throw
                    return                                                         # an exception
                text = text.decode('utf-8')
                text = re.sub("[^a-zA-Z.+3]"," ", text)  # Now get rid of any terms that aren't words (include 3 for d3.js)
                                                        # Also include + for C++        

                text = text.lower().split()  # Go to lower case and split them apart
                stop_words = set(stopwords.words("english")) # Filter out any stop words
                text = [w for w in text if not w in stop_words]
                text = list(set(text)) # Last, just get the set of these. Ignore counts (we are just looking at whether a term existed
                                   # or not on the website)
                text_testData = " ".join(str(x) for x in text)
                job_description_unclean.append(text_testData)
                for i in range(0, len(text)):
                    text[i] = ps.stem(lemma.lemmatize(text[i]))
                job_description.append(text)
                print('In the process.....')
        # Key for the dictionary
    for i in range(0, len(companies)):
        companies[i] = companies[i]+"-"+job_post[i]
    print("In the process.........")
    # List of job title and description in a preprocessed manner
    columns = ["Job-Title","Description"]
    sample_df = pd.DataFrame(columns = columns)
    for i in range(0, len(companies)):
        testData = []
        testData.append(companies[i])
        testData.append(job_description_unclean[i])
        num = len(sample_df)+1
        posting = {'Job-Title' : companies[i], 'Description' : job_description[i]}
        sample_df.loc[num] = testData
        preProcessedPostings.append(posting)
        print('In the process.....',i)
    # print(sample_df)
    
    #saving sample_df as a local csv file — define your own local path to save contents 
    sample_df.to_csv(str(sys.argv[1]), sep=',')
    print("Finished storing the preprocessed data into csv file ......")
extract_links_from_result()


# In[2]:

def insertInDB(preProcessedPostings):  
    con = mongo.MongoClient(host='127.0.0.1', port=3001)
    db = con['meteor']
    cleanPostings_stem_test = db['cleanPostings_stem_test']
    db.cleanPostings_stem_test.insert_many(preProcessedPostings)
# insertInDB(preProcessedPostings)


# In[3]:

def excelInMongoDB():
    file = str(sys.argv[2])
    xl = pd.ExcelFile(file) 
    df1 = xl.parse('Sample_Dataset_1')
    d = df1.to_dict(orient='records')
    insertInDB(d)
excelInMongoDB()


# In[17]:

def viewDB():
    con = mongo.MongoClient(host='127.0.0.1', port=3001)
    db = con['meteor']
    cleanPostings_stem_test = db['cleanPostings_stem_test']
    result = cleanPostings_stem_test.find()
    for record in result:
        print(record['Job-Title'] + ',',record['Description'])
viewDB() 


# In[ ]:



