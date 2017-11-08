import csv
import re

#reads in .txt file
#ensure .txt file is in the same location or folder as main.py
txtfile = open('Paragraph_1.txt', mode ='r')
txtfileStore = txtfile.read()

#gets list of all the words (that which is separated by a space)
Words = txtfileStore.split(' ')

#loop through list to get word count
wordCnt = 0
for i in Words:
    wordCnt += 1

#get sentence count
'''The code below works, but I do not understand it '''
sentences =  re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', txtfileStore)


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


#prints the results
print('Paragraph Analysis')
print('------------------')
print('Approximate Word Count: ' + str(wordCnt))
print('Approximate Sentence Count: ' + str(sentCnt))
print('Average Letter Count: ' + str(avgLettCt))
print('Average Sentence Length: ' + str(avgSenLen))


