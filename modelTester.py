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
            lineWordsList = re.split(r'\,?\"?\`?\:?\;?(\!?)(\??)(\.?)\s?', line.lower())
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
        CHW = history + " " + word
        try:
            if self.trainingData[history] != 0:
                return self.trainingData[CHW] / self.trainingData[history]
        except KeyError:
            return 0

    def __processPerplexityOfModel(self):

        perplexity = len(self.trainingData)

        for wordIterator in range(1, self.wordsList.__len__()):
            perplexity = perplexity * self.__getLikelihood(self.__getHistory(wordIterator), self.wordsList[wordIterator])

        perplexity = math.pow(perplexity, 1/self.wordsList.__len__())

        return perplexity