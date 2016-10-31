import operator
import copy
import math

class Model:

    def __init__(self, modelOrder, nGramList):
        self.modelOrder = modelOrder
        self.nGramList = nGramList

    def printModel(self):
        print str(self.nGramList[self.modelOrder - 1])

    def getWordTypeCount(self):
        return self.nGramList[0].__len__()

    def printLexiconCount(self):
        print "Model order : " + str(self.modelOrder) + " lexicon count : " + str(self.nGramList[self.modelOrder - 1].__len__())

    def getLexiconCount(self):
        return self.nGramList[self.modelOrder - 1].__len__()

    def printTwentyMoreFrequentLexicon(self):
        maxValues = []
        nGramCopy = copy.copy(self.nGramList[self.modelOrder - 1])
        maximums = 0
        while maximums < 20:
            maxLexicon = max(nGramCopy.iteritems(), key=operator.itemgetter(1))
            if "</s>" not in maxLexicon[0] and maxLexicon[0] != "<UNK>":
                maxValues.append(maxLexicon)
                maximums += 1
            del nGramCopy[maxLexicon[0]]

        print "Model order : " + str(self.modelOrder)
        for maxValue in maxValues:
            print "Word type : " + str(maxValue[0]) + " - " + "Occurence : " + str(maxValue[1])

    def laplaceLikelihood(self, w, h):
        CHW = self.getCHW(h, w)
        print "CHW : " + str(CHW)
        CH = self.getCH(h)
        print "CH " + str(CH)
        WCount = self.getWordTypeCount()
        return math.log(float(CHW + 1) / float(CH + WCount), 2)

    def backOffLikelihood(self, w, h):
        CHW = self.getCHW(h, w)
        CH = self.getCH(h)
        WCount = self.getWordTypeCount()
        if CHW > 0:
            return math.log(float(CHW) / float(CH))
        elif CHW == 0 and CH > 0 and h.split(' ', 1).__len__() > 1:
            CHW = self.getCHW(h.split(' ', 1)[1], w)
            if CHW > 0:
                return math.log((float(CHW) / float(CH)), 2)
            else:
                return math.log((1.0 / float(WCount)), 2)
        else:
            return math.log((1.0 / float(WCount)), 2)

    def getCHW(self, h, w):
        lexicon = h + " " + w
        if self.nGramList[self.modelOrder - 1].has_key(lexicon):
            return self.nGramList[self.modelOrder - 1][lexicon]
        return 0

    def getCH(self, h):
        if self.nGramList[self.modelOrder - 2].has_key(h):
            return self.nGramList[self.modelOrder - 2][h]
        return 0

    def hasKey(self, key):
        return self.nGramList[self.modelOrder - 1].has_key(key)
