'''
Created on 21 oct. 2016

@author: anne-francevanswieten
'''
from Parser import Parser
from modelTester import ModelTester
import re

def removeEmptyCharacter(wordsList):
    print wordsList.remove('')
    print "Passe ici"

if __name__ == '__main__':
    parser = Parser()

    parser.count_wordfile()
    parser.lexicon_aumoinstrois()

    parser.standardinazionfile()
    parser.mesgram()
    parser.statgram()
    
    
    
    parser.genbiramTest()
    parser.gentriramTest()
    parser.prob_Add_One_Unigrams()
    parser.prob_Add_One_Bigrams()
    parser.prob_Add_One_Trigrams()

    print(parser.verifProb())

    # trainingData = dict(parser.dictUnigrame, **parser.dictBigrame)
    # trainingData = dict(trainingData, **parser.dictTrigrame)

    trainingData = dict(parser.dictProbUnigrame, **parser.dictProbBigrame)
    trainingData = dict(trainingData, **parser.dictTrigrame)

    myTester = ModelTester(trainingData)
    print "Perplexity : " + str(myTester.getPerplexity("Dumas_test.txt"))
