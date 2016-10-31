import re
import math
from Parser import Parser

class ModelTester:

    def __init__(self, parser):
        self.parser = parser

    def getPerplexity(self, model, smoothingType):
        self.model = model
        wordsList = self.parser.getListOfWordsInFile()
        return self.__processPerplexityOfModel(wordsList, smoothingType)

    def __getHistory(self, wordPositionInList, wordsList):
        history = ""
        if wordPositionInList == 0:
            return history
        elif wordPositionInList == 1:
            return wordsList[0]
        for wordHistory in range(wordPositionInList - (self.model.modelOrder - 1), wordPositionInList):
            history += wordsList[wordHistory] + " "
        history = history[:-1]
        return history

    def __processPerplexityOfModel(self, wordsList, smoothingType):
        logLikelihood = 0
        if smoothingType == "laplace":
            for wordIterator in range(self.model.modelOrder - 1, wordsList.__len__()):
                logLikelihood += self.model.laplaceLikelihood(wordsList[wordIterator], self.__getHistory(wordIterator, wordsList))
        elif smoothingType == "backoff":
            for wordIterator in range(self.model.modelOrder - 1, wordsList.__len__()):
                logLikelihood += self.model.backOffLikelihood(wordsList[wordIterator], self.__getHistory(wordIterator, wordsList))

        logLikelihood = float(logLikelihood / float(wordsList.__len__()))
        perplexity = math.pow(2, -float(logLikelihood))

        return perplexity
