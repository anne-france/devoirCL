from model import Model

class ModelTrainer:

    def __init__(self, parser):
        self.parser = parser

    def train(self, modelOrder):
        nGramList = []
        if modelOrder == 1:
            uniGram = self.deleteUnderThreeOccurenceElements(self.parser.getUnigram())
            nGramList.append(uniGram)
            model = Model(modelOrder, nGramList)
            return model
        else:
            uniGram = self.deleteUnderThreeOccurenceElements(self.parser.getUnigram())
            gramData = uniGram
            nGramList.append(uniGram)
            for n in range(2, modelOrder + 1):
                nGram = self.parser.getNGram(n, uniGram)
                nGramList.append(nGram)
            model = Model(modelOrder, nGramList)
            return model

    def deleteUnderThreeOccurenceElements(self, uniGram):
        uniGram["<UNK>"] = 0
        for word in uniGram.keys():
            if uniGram[word] < 3:
                uniGram["<UNK>"] += uniGram[word]
                del uniGram[word]
        return uniGram

    def setNGramWordOccuringUnderThreeTimesToUnk(self, deletedWordList, nGram):
        print nGram.__len__()
        for lexicon in nGram.keys():
            wordsInLexicon = lexicon.split(' ', 1)
            newLexicon = ""
            for word in range(0, wordsInLexicon.__len__()):
                if wordsInLexicon[word] in deletedWordList:
                    wordsInLexicon[word] = "</UNK>"
                newLexicon += wordsInLexicon[word] + " "
            newLexicon = newLexicon[:-1]
            lexiconOccurence = nGram[lexicon]
            del nGram[lexicon]
            nGram[newLexicon] = lexiconOccurence
        return nGram




