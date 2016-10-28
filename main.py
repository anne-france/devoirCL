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

    trainingData = dict(parser.dictUnigrame, **parser.dictBigrame)
    trainingData = dict(trainingData, **parser.dictTrigrame)

    print str(trainingData[('the','cat')])
    myTester = ModelTester(trainingData)
    print "Perplexity : " + str(myTester.getPerplexity("Dumas_test.txt"))

