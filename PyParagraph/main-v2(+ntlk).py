import csv
import re
import nltk

#reads in .txt file
#ensure .txt file is in the same location or folder as main.py
txtfile = open('Paragraph_2.txt', mode ='r')
txtfileStore = txtfile.read()

#gets list of all the words (that which is separated by a space)
Words = txtfileStore.split(' ')

#loop through list to get word count
wordCnt = 0
for i in Words:
    wordCnt += 1

#get sentence count
'''The code below gets me close (exception: stores empty item at end of list).
However, I do not know what exactly is going on so I can't fix the code. 
sentences =  re.split(r' *[\.\?!][\'"\)\]]* *', txtfileStore)'''

sentences = nltk.sent_tokenize(txtfileStore)

#loop through sentence list to get sentence count
sentCnt = 0
for i in sentences:
	sentCnt += 1

#get average letter count per word
letters = []
for i in Words:
    wordLen  = len(i)
    letters.append(wordLen)

avgLettCt = sum(letters)/wordCnt

#get average sentence length per word
avgSenLen = wordCnt/sentCnt    

'''
#prints the results
print('Paragraph Analysis')
print('------------------')
print('Approximate Word Count: ' + str(wordCnt))
print('Approximate Sentence Count: ' + str(sentCnt))
print('Average Letter Count: ' + str(avgLettCt))
print('Average Sentence Length: ' + str(avgSenLen))
'''
#debug test
print(sentences)

