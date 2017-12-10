
# coding: utf-8

# In[1]:

import pymongo as mongo
import PyPDF2 as pdfreader
import pprint
import glob, os
import sys


# In[2]:

def getPDFContent(path):
    "Extract text from PDF document"
    content = ""
    p = open(path, "rb")
    if ( not pdfreader.PdfFileReader(p).isEncrypted):
        pdf = pdfreader.PdfFileReader(p)
        content += pdf.getPage(0).extractText() + "\n"
        content = " ".join(content.replace(u"\xa0", " ").strip().split())
        return content    
    else:
        print("File is encrypted")


# In[3]:

def insertInDB(resumeDocument):
    con = mongo.MongoClient(host='127.0.0.1', port=3001)
    db = con['meteor']
    resume_test = db['resume_temp']
    db.resume_test.insert_many(resumeDocument)


# In[4]:

def getFiles(dirPath):
    rDocuments = []
    for filename in os.listdir(dirPath):
        if filename.endswith(".pdf"):
            file = os.path.join(dirPath, filename)
            pdfl = getPDFContent(file).encode("ascii", "ignore")
            print(pdfl)
            rDocuments.append({'Name': filename[:-4],'Content': pdfl})
    insertInDB(rDocuments)


# In[5]:

getFiles(sys.argv[1])


# In[6]:

def viewDB():
    con = mongo.MongoClient(host='127.0.0.1', port=3001)
    db = con['meteor']
    resume_test = db['resume_temp']
    result = resume_test.find()
    for record in result:
        print(record['Name'] + ',',record['Content'])
viewDB()   


# In[ ]:



