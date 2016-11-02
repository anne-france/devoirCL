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
        CH = self.getCH(h)
        WCount = self.getWordTypeCount()
        return float(CHW + 1) / float(CH + WCount)

    def backOffLikelihood(self, w, h):
        CHW = self.getCHW(h, w)
        CH = self.getCH(h)
        WCount = self.getWordTypeCount()
        if CHW > 0:
            return float(CHW) / float(CH)
        elif CHW == 0 and CH > 0 and h.split(' ', 1).__len__() > 1:
            CHW = self.getCHW(h.split(' ', 1)[1], w)
            if CHW > 0:
                return (float(CHW) / float(CH))
            else:
                return (1.0 / float(WCount))
        else:
            return (1.0 / float(WCount))

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
    
    def statCvs(self):
        dicoStat={}       
        for v in self.nGramList[self.modelOrder - 1].itervalues():        
            if dicoStat.has_key(v):                   
                dicoStat[v] = dicoStat[v] +1
            else :
                dicoStat[v]= 1  
        sortedlist= sorted(dicoStat.items(), key=lambda t: t[0])
        fwriterbi = open("StatGramme_"+ str(self.modelOrder) +".csv","w") 
        for entry in sortedlist:
            fwriterbi.write(str(entry[0]) +"," + str(entry[1])+"\n")    
        fwriterbi.close

    def playShannonGame(self, stringToComplete):
        tenMoreProbable = []
        stringToCompleteWordsList = stringToComplete.split(" ")
        analyseFirstWordPosition = stringToCompleteWordsList.__len__() - self.modelOrder + 1
        history = ""
        for wordPosition in range(analyseFirstWordPosition, stringToCompleteWordsList.__len__()):
            history += stringToCompleteWordsList[wordPosition] + " "
        history = history[:-1]
        probability = {}
        for word in self.nGramList[0]:
            likelihood = self.backOffLikelihood(word, history)
            probability[word] = likelihood

        maxValues = []
        probabilityCopy = copy.copy(probability)
        maximums = 0
        moreThenDartagnan = 0

        for word, value in probabilityCopy.iteritems():
            if value > probabilityCopy["d'artagnan"]:
                moreThenDartagnan += 1

        print "D'artagnan would be in position " + str(moreThenDartagnan + 1) + " and would have a probability of " + str(probabilityCopy["d'artagnan"])

        while maximums < 10:
            maxLexicon = max(probabilityCopy.iteritems(), key=operator.itemgetter(1))
            if "</s>" not in maxLexicon[0] and maxLexicon[0] != "<UNK>":
                maxValues.append(maxLexicon)
                maximums += 1
            del probabilityCopy[maxLexicon[0]]

        for word in maxValues:
            print word[0] + " have a " + str(probability[word[0]]) + " likelihood"





        
        
