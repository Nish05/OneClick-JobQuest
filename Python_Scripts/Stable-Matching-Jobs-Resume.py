
# coding: utf-8

# In[3]:

def checkHigherPreference(preferenceList, currentResume, newCandidate, oldCandidate):
    for i in range(0, len(preferenceList[0])) :
        if(preferenceList[currentResume][i] == oldCandidate) :
            return True
        if(preferenceList[currentResume][i] == newCandidate) :
            return False


# In[1]:


def stableMatch(preferenceList, candidates, total_job_resume):
    resumes = [-1] * candidates
    freeEmployers = [False] * candidates
    
    freeCount = candidates
    while freeCount > 0 :
        job = 0
        for i in range (0, candidates) :
            if (freeEmployers[i] == False) :
                job = i 
                break
  
        for i in range (0, candidates) :
        
            if (freeEmployers[job] == True):
                break
            currentResume = preferenceList[job][i]
            if (resumes[currentResume - candidates] == -1) :
                    resumes[currentResume - candidates] = job
                    freeEmployers[job] = True
                    freeCount= freeCount - 1
            else :
                oldJob = resumes[currentResume - candidates]
                otherPreference = checkHigherPreference(preferenceList,currentResume, job, oldJob)
                if( otherPreference == False ) :
                    resumes[currentResume - candidates] = job
                    freeEmployers[job] = True
                    freeEmployers[oldJob] = False
    print("Resumes  Jobs")               
    for i in range(0, candidates):
        print(i+candidates," ",resumes[i])
                  


# In[2]:

def main():
    preferenceList = [[7, 5, 6, 4], [5, 4, 6, 7], [4, 5, 6, 7], [4, 5, 6, 7],
                      [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
    stableMatch(preferenceList, len(preferenceList[0]), len(preferenceList))
main()
list_of_resume = {}


# In[ ]:



