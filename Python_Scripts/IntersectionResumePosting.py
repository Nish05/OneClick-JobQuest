
# coding: utf-8

# In[1]:

import pymongo as mongo
import scipy as sp
from scipy import stats
import pandas as pd


# In[2]:

con = mongo.MongoClient(host='127.0.0.1', port=3001)
db = con['meteor']
cleanResume_stem_test = db['cleanResume_stem_test']
cleanPostings_stem_test = db['cleanPostings_stem_test']
resumes = cleanResume_stem_test.find()
postings = cleanPostings_stem_test.find()
generateRanks = []
dataframes = []


# In[3]:

def checkElements(pContent, rContent):
    pContent.sort()
    rContent.sort()
    i = 0 
    j = 0
    pLen = len(pContent)
    rLen = len(rContent)
    score = 0
    
    while( i < pLen and j < rLen):
        if(pContent[i] < rContent[j]): i = i+1
        elif(pContent[i] > rContent[j]): j= j+1
        else : 
            score += 1
            i = i+1
            j = j+1
            
    return score


# In[4]:

def insertNameScore(score, name, rName, rScore):
    i = 0
#     print(score)
#     print(name)
    length = len(rScore)
    if(length == 0):
        rScore.append(score)
        rName.append(name)
        return rScore,rName
    
    while( i < length-1 ):
        if(rScore[i] > score):
            rScore = rScore[:i] + [score] + rScore[i:]
            rName = rName[:i] + [name] + rName[i:]
            
        elif(rScore[i] <= score and rScore[i+1] >= score):
            rScore = rScore[:i] + [score] + rScore[i+1:]
            rName = rName[:i] + [name] + rName[i+1:]
        i = i+1
            
    return rScore, rName
    


# In[5]:

def intersectionEmp(resumes, postings):
    rankedList =[]
    rDocuments = list(resumes)
    pDocuments = list(postings)
    
    for resume in rDocuments:
        rContent = resume['Content']
        name = resume['Name']
        rLength = len(rContent)
        i = 0     
#         print('Candidate Name', name, 'Total keywords : ',rLength)
        pName =[]
        pScore=[]
        spDict = {}
        for posting in pDocuments:
            pContent = posting['Description'].split()
            pTitle = posting['Job-Title']
            score = checkElements(pContent, rContent)
            pName.append(pTitle)
            pScore.append(score)
#             print(i ,' ', name)
            i = i + 1
#         print('Posting : ', pTitle)
        averageScore = []
        for k in range (0,len(pName)):
            averageScore.append((pScore[k]/rLength))
            
        spScore, spName = zip(*sorted(zip(averageScore, pName)))
        spScore = spScore[::-1]
        spName = spName[::-1]
#         spScore = list(spScore).reverse()
#         spName = list(spName).reverse()
        
        for l in range(0,len(spName)):
            spDict[spName[l]] = l+1
        
#             print('Job Title : ',spName[l], 'Score :',spScore[l])
#         print(spDict)
        generateRanks.append(spDict)
#             print('Posting : ',pTitle,' Resume : ',name, '-> Score :',score)
intersectionEmp(resumes, postings)

print(generateRanks)


# In[10]:

# org_rank = [1,2,4,6,7,9]
# cal_rank = [4,2,9,6,2,1]
def calculateKendallTau(org_rank, cal_rank):
    tau, p_value = sp.stats.kendalltau(org_rank, cal_rank)
    print("Tau : ", tau)
    print("P_value : ", p_value)
# calculateKendallTau(org_rank, cal_rank)


# In[6]:

def excelInMongoDB():
    file = '/Users/Nish/Documents/Acadamic-RIT/Fall 2017/Project/Testing/Sample_Dataset_1.xls'
    xl = pd.ExcelFile(file) 
    df1 = xl.parse('Krupa_Shah')
    dataframes.append(df1)
    df2 = xl.parse('Forum_Kapadia')
    dataframes.append(df2)
    df3 = xl.parse('Mansee_Jadhav')
    dataframes.append(df3)
    df4 = xl.parse('Vinay_More')
    dataframes.append(df4)
    df5 = xl.parse('Amrut_Shenoy')
    dataframes.append(df5)    
excelInMongoDB()


# In[11]:

def rankingLists():
    for i in range(0, (len(generateRanks)-1)):
        currentDict = generateRanks[i]
        currentDataframe = dataframes[i]
        orgRanking = []
        computedRanking = []
        for index,row in currentDataframe.iterrows():
            title = row['Job Title']
            calrank = currentDict.get(title)
            computedRanking.append(calrank)
            orgRanking.append(row['Ranking'])
        calculateKendallTau(orgRanking, computedRanking)
            
        
        
rankingLists()


# In[ ]:



