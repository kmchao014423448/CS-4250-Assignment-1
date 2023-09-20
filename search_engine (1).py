#!/usr/bin/env python
# coding: utf-8

# In[12]:


#-------------------------------------------------------------------------
# AUTHOR: Kyle Chao
# FILENAME: search_engine
# SPECIFICATION: Submission for #8 on Assignment 1
# FOR: CS 4250- Assignment #1
# TIME SPENT: 42 Hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#importing some Python libraries
import csv
import math

documents = []
labels = []

#reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            documents.append (row[0])
            labels.append(row[1])

            
#Conduct stopword removal.
#--> add your Python code here
stopWords = {'I', 'and', 'She', 'They', 'her', 'their'}

            
            
count=0

for a in documents:

   # print(a)
    for i in stopWords:
        
        #print(i)
        if i in a:
            #print(count)
            #print('yes')
            a = a.replace(i,'')
            #print(a)
            documents[count] = a
    count= count + 1
            
            

         
#Conduct stemming.
#--> add your Python code here
steeming = {
  "cats": "cat",
  "dogs": "dog",
  "loves": "love",
}
counter = 0
for a in documents:
    #print(a)
    for key in steeming:
        if key in a:
            #print('yes')
            a = a.replace(key,steeming[key])
            #print(a)
            documents[counter] = a

    counter = counter + 1
    
#print(documents)

#Identify the index terms.
#--> add your Python code here
terms = []
print('Enter your query:')


query = input()
print('')

terms = query.split()



counta=0
for a in terms:

    for i in stopWords:
        
        #print(i)
        if i in terms:
            a = a.replace(i,'')
            #print(a)
            terms[counta] = a
    counta= counta + 1



     
    
  

counting=0

for a in terms:
    #print(a)
    for key in steeming:
        if key in a:
            #print('yes')
            a = a.replace(key,steeming[key])
            terms[counting] = a

    counting = counting + 1

if '' in terms:

    terms.remove('')

print('Tokenized query: ',terms)
print('')

print('Tokenized documents: ',documents)
print('')

#Build the tf-idf term weights matrix.
#--> add your Python code here
docMatrix = []



row = len(documents)
a = ''

columns=str()
for a in documents:
    columns= columns + a



x= columns.split()

term= []
for a in x:
    if a not in term:
        term.append(a)



column = len(term)



docMatrix= [[' '] + term]



county=1
for a in range(row):
    lit = []
    lit = ['d'+str(county)] + (['']*column) 
    docMatrix.append(lit)
    county=county+1
    

    


catcount=0
dogcount=0
lovecount=0
    
    
for a in documents:
    if 'cat' in a:
        catcount= catcount+1
    if 'dog' in a:
        dogcount=dogcount+1
    if 'love' in a:
        lovecount=lovecount +1


countset = 1


tfidf = []
loveidf=[]
catidf=[]
dogidf=[]

for a in documents:
    b=a.split()
    #print(len(b))
    countmove = 1
    cat= 0
    dog= 0
    love= 0
    x= columns.split()
    cat = (a.count('cat'))
    dog = (a.count('dog'))
    love = (a.count('love'))
    
    
    
    tfcat = cat/len(b)
    idfcat = math.log10(row/catcount)
    tfidfcat = tfcat*idfcat
    
    
    tfdog = dog/len(b)
    idfdog = math.log10(row/dogcount)
    tfidfdog = tfdog*idfdog
    
    
    tflove = love/len(b)
    idflove = math.log10(row/lovecount)
    tfidflove = tflove*idflove
    
    loveidf.append(tfidflove)
    catidf.append(tfidfcat)
    dogidf.append(tfidfdog)
    tfidf.append(tfidflove)
    tfidf.append(tfidfcat)
    tfidf.append(tfidfdog)


setcount=1
movecount=1
throughcount=0

for a in range(len(tfidf)):
    docMatrix[setcount][movecount]=tfidf[throughcount]
    movecount = movecount +1
    throughcount = throughcount + 1
    if movecount ==4:
        movecount =1
        setcount = setcount + 1
    if throughcount > 8:
        break
    

    

print('tfidf Matrix: ',docMatrix)   
print('')

    
#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []




countidf=0
for a in range (len(catidf)):
    docScores.append(loveidf[countidf]+catidf[countidf]+dogidf[countidf])
    countidf=countidf+1

#print(docScores)

#term vs terms

doccount=0
for a in range(len(docScores)):
    print('Score for Document',doccount+1,': ',docScores[doccount])
    doccount=doccount+1
binterm=[]
countterms=0
for a in term:
    if a in terms:
        binterm.append(1)
    else:
        binterm.append(0)
print('')
print('binary query: ',binterm)
print('')
#print(docScores)
    
#Calculate and print the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
#--> add your Python code here

retrievedoc=[]
rcount=1

for a in docScores:
    if a > .1:
        retrievedoc.append(rcount)
    #print(rcount)
    rcount=rcount+1
    
reldoc=[]
ccount=0
for a in term:
    for b in term:
        if a in b:
            reldoc.append(ccount+1)
            
            
    ccount=ccount+1

    
#print(documents)        

#print(terms)
#print(reldoc)
hitdoc=[]
acount=0
for a in reldoc:
    if docScores[acount]>.1:
        hitdoc.append(a)
    acount=acount+1    
print('The relevant documents with a score greater than .1 are: ',hitdoc)

  







preclist=[]
for a in terms:
    pcount=1
    for x in documents:
        if a in x:
            preclist.append(pcount)
        pcount=pcount+1
    


plist=[]


for a in set(preclist):
    #print(int(a))
    if docScores[int(a)-1]>.1:
        plist.append(a)

flist=[]
hcount=0

for a in plist:
    if a == hitdoc[hcount]:
        flist.append(1)
    else:
        flist.append(0)
    hcount=hcount+1
gcount=0
fcount=0
for a in flist:
    fcount=fcount+1
    gcount=int(a) + gcount

    

recall=gcount/fcount

rlist=[]


checkdoc=[]
for a in documents:
    c=a.split()
    checkdoc.append(c)
#print(checkdoc)

for a in hitdoc:
    if any(x in terms for x in checkdoc[int(a)-1]):
        rlist.append(1)
    else:
        rlist.append(0)

                
#print(rlist)
rcount=0
gcount=0
for a in rlist:
    rcount=rcount+1
    gcount=int(a)+gcount
    
precision=gcount/rcount

print('The precision of this engine is: ',precision*100,'%')
print('The recall of this engine is: ',recall*100,'%')



# In[ ]:




