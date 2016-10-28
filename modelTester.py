import re
import math

class ModelTester:

    def __init__(self, trainingData):
        self.trainingData = trainingData

    def getPerplexity(self, testFileName):
        testFile = open(testFileName,"r")
        wordsList = self.__getListOfWords(testFile)
        self.wordsList = self.__parsePunctuation(wordsList)
        perplexity = self.__processPerplexityOfModel()
        return perplexity

    def __getListOfWords(self, file):
        totalWordList = []
        for line in file:
            lineWordsList = re.split(r'\,?\"?\`?-?\:?\;?(\!?)(\??)(\.?)\s?', line.lower())
            listLength = lineWordsList.__len__()
            word = 0
            while word < listLength:
                if lineWordsList[word] == '':
                    lineWordsList.remove('')
                    word -= 1
                    listLength -= 1
                word += 1

            totalWordList = totalWordList + lineWordsList

        return totalWordList

    def __parsePunctuation(self, wordList):
        for word in range(0, wordList.__len__()):
            if wordList[word] == "!" or wordList[word] == "." or wordList[word] == "?":
                wordList[word] = "</s>"
        return wordList

    def __getHistory(self, wordPositionInList):
        history = []
        if wordPositionInList == 0:
            return None
        elif wordPositionInList == 1:
            return self.wordsList[0]
        for wordHistory in range(wordPositionInList - 2, wordPositionInList):
            history.append(self.wordsList[wordHistory])
        historyString = history[0] + " " + history[1]
        return historyString

    def __getLikelihood(self, history, word):
        historySplit = history.split(' ')
        if not self.trainingData.has_key((word,)):
            word = "<UNK>"
        if historySplit.__len__() == 1:
            if not self.trainingData.has_key((historySplit[0],)):
                historySplit[0] = "<UNK>"
            CHW = (historySplit[0], word)
        else:
            if not self.trainingData.has_key((historySplit[0],)):
                historySplit[0] = "<UNK>"
            if not self.trainingData.has_key((historySplit[1], )):
                historySplit[1] = "<UNK>"
            history = (historySplit[0], historySplit[1])
            CHW = (historySplit[0], historySplit[1], word)

        if self.trainingData.has_key(history) and self.trainingData.has_key(CHW):
            print self.trainingData[history]
            print self.trainingData
            return math.log(float(float(self.trainingData[CHW]) / float(self.trainingData[history])), 2)
        else:
            return math.log(1.0/13200.0, 2)

    def __processPerplexityOfModel(self):

        i = float(1.0/13200.0)
        logLikelihood = math.log(i, 2)

        for wordIterator in range(1, self.wordsList.__len__()):
            logLikelihood += self.__getLikelihood(self.__getHistory(wordIterator), self.wordsList[wordIterator])

        logLikelihood = float(logLikelihood / float(self.wordsList.__len__()))
        perplexity = math.pow(2, -float(logLikelihood))

        return perplexity
