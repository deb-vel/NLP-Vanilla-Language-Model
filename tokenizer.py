import codecs
import random

#writes N-Grams' details
def writeToFile(nGram, Freq, Prob):
    file.write(nGram) #N-Gram
    file.write(" ") #delimiter
    file.write(str(Freq)) #frequency of n-gram
    file.write(" ") #delimeter
    file.write(str(Prob)) #probability of n-gram
    file.write("\n")#new line for next n-gram's details

with open('malti03.academic.1.txt', 'r') as file:
    # gets first word from each line in text file and decode it using utf8 to recognize maltese characters
    wordlist = [line.encode("windows-1252").decode('utf8').split(None, 1)[0] for line in file]

sentences = [] #stores all sentences

#this creates a 2D array of sentences
for i, word in enumerate(wordlist):
    if word == '<s':
        sentence = []
        index = i+1

        while wordlist[index] != '</s>': #start getting the sentence word by word till it meets end of sentence
            sentence.append(wordlist[index]) #append current word
            index += 1 #to access next word
        sentences.append(sentence) #append to a 2D array of sentences

random.shuffle(sentences) #randomly shuffle sentences in array
trainingData = sentences[0:round((80/100)*len(sentences))] #get the first 80 percent
testingData = sentences[round((80/100)*len(sentences)):len(sentences)] # get the rest


file = codecs.open("trainingSet.txt", "w","utf-8") #opens file that will store training set
#populate file placing each word in a new line
for i in range(len(trainingData)):
    for j in range(len(trainingData[i])):
        file.write(trainingData[i][j])
        file.write("\n")
file = codecs.open("testSet.txt", "w","utf-8") #opens file that will store testing set
#populate file placing each word in a new line
for i in range(len(testingData)):
    for j in range(len(testingData[i])):
        file.write(testingData[i][j])
        file.write("\n")


#-----FOR UNIGRAM------

file = codecs.open("unigram.txt", "w","utf-8") #opens file that will store unigrams' details

words = [] #stores unique words
frequency = [] #stores frequency for each word
wordCount = 0

#loop through the whole 2D array sentence by sentence word by word
for i in range(len(trainingData)):
    for j in range(len(trainingData[i])):
        wordCount+=1 #counts number of words in the corpus. Will be used to calculate the unigrams' probabilities
        if(trainingData[i][j] not in words): #if the unigram is unique
            words.append(trainingData[i][j]) # append unigram to the list of unique words
            frequency.append(1)  # add to array of frequencies
        else: #if unigram already met
            frequency[words.index(trainingData[i][j])] += 1 #increase its frequency

#display the details for each unigram
for k in range(len(words)):
    wordprobability = frequency[k] / wordCount  # calculates the probability
    print(words[k], "\t\t\t\tFrekwenza: ",frequency[k], "\t\t\t\tProbabbilita: ",wordprobability)  # print calculations
    writeToFile(words[k], frequency[k], wordprobability)  # write results to unigram text file'



#-----FOR BIGRAM------
w2 = 1 #counter for the next word
bigrams = [] #stores all unique bigrams
bigramFrequency = [] #stores bigrams' frequencies
currentWords = [] #stores first word of bigram
nextWords = [] #stores second word of bigram

file =  codecs.open("bigram.txt", "w", "utf-8") #open bigram.txt

#loop through 2D array
for i in range(len(trainingData)):
    w2 = 1 #Counter for the next word
    for j in range(len(trainingData[i])):
        #countOfTwoWords = 0 #initialized to zero for every new iteration. will store the frequency of the bigram
        currentWord = trainingData[i][j] #take first word
        if (j < len(trainingData[i]) - 1): #to make sure we do not access an index which does not exist
            nextWord = trainingData[i][w2] #take the next word
        bigram = currentWord + " "+nextWord #join the two word into one whole bigram

        if bigram not in bigrams: #if the bigram found above is not in the list of bigrams. i.e. if bigram not met yet
            #append words and frequencies to their respective arrays
            nextWords.append(nextWord)
            currentWords.append(currentWord)
            bigrams.append(bigram) #append the bigram to the list of unique bigrams
            bigramFrequency.append(1)
        else: #if bigram already met
            bigramFrequency[bigrams.index(bigram)] += 1 #increment frequency

        w2+=1 #increment for next iteration

#loop through list of unique bigrams
for k in range(len(bigrams)):
    currentWord = currentWords[k] #get first word of bigram
    nextWord = nextWords[k] #get second word of bigram
    indexNo = words.index(currentWord)  # get the position where the first word of bigram is found in the list of unique words
    freq = frequency[indexNo]  # access the frequency of the word by using the index found above
    probability = bigramFrequency[k] / freq  # calculate probability
    print("P(", nextWord, "|", currentWord, ")= ", probability, "\t\t\t\t\t\tFrekwenza ta' \"", bigrams[k], "\": ",
          bigramFrequency[k])  # print results
    writeToFile(bigrams[k], bigramFrequency[k], probability)  # write results to bigram text file'



#------FOR TRIGRAM------

w2 = 1 #Counter for the next word
w3 = 2 #counter for the third word
trigramFrequency = []  # stores trigrams' frequencies
currentWords = [] # stores 1st words of trigram
secondWords = [] #stores 2nd words of trigram
thirdWords=[] #stores thord words of trigram
trigrams = [] #stores all unique trigrams

file = codecs.open("trigram.txt", "w", "utf-8") #opens trigram text file

#loop through all 2D array
for i in range(len(trainingData)):
    w2 = 1  # Set back to one when iterating through next row
    w3 = 2 #Set back to 2 when iterating through a new row
    for j in range(len(trainingData[i])):
        #countofThreeWords = 0  # initialized to zero for every new iteration. will store the frequency of the bigram
        currentWord = trainingData[i][j]  # take first word
        if (j < len(trainingData[i]) - 2):  # to make sure we do not access an index which does not exist
            secondWord = trainingData[i][w2]  # take the next word
            thirdWord = trainingData[i][w3] #take the third word
            trigram = currentWord + " " + secondWord + " " + thirdWord  # join all three words into one string

        if trigram not in trigrams: #if a new trigram is met
            trigrams.append(trigram) #add the trigram to the list of unique trigrams
            #append words and frequencies to their corresponding arrays to be accessed later
            secondWords.append(secondWord)
            thirdWords.append(thirdWord)
            currentWords.append(currentWord)
            trigramFrequency.append(1)
        else:
            trigramFrequency[trigrams.index(trigram)] += 1 #increment frequency if trigram already exists
        w2+=1 #increment for next iteration
        w3+=1

#loops through all unique trigrams
for k in range(len(trigrams)):
    #get all three individual words of trigram
    currentWord = currentWords[k]
    secondWord = secondWords[k]
    thirdWord = thirdWords[k]
    bigram = currentWord+" "+secondWord #join them as one string
    if bigram in bigrams:
        indexNo = bigrams.index(bigram) #get the index where that bigram is found in list of unique bigrams
    freq = bigramFrequency[indexNo]  # access the frequency of the bigram by using the index found above
    probability = trigramFrequency[k] / freq  # calculate probability
    print("P(", thirdWord, "|", currentWord, " ", secondWord, ")= ", probability, "\t\t\t\t\t\tFrekwenza ta' \"",
              trigrams[k], "\" : ", trigramFrequency[k])  # print results
    writeToFile(trigrams[k], trigramFrequency[k], probability)  # write results to trigram text file'
    
input("Press enter to exit") #keeps cmd window open