'''
Created on 21 oct. 2016

@author: anne-francevanswieten
'''
from Parser import Parser


if __name__ == '__main__':
    parser = Parser()

    parser.count_wordfile()
    parser.lexicon_aumoinstrois()


    parser.standardinazionfile()
    parser.mesgram()

    test3Gram = {}
    test2Gram = {}
    test3Gram["for this is"] = 3
    test3Gram["for this chair"] = 7
    test3Gram["for this car"] = 4
    test2Gram["for this"] = 14
    test2Gram["this is"] = 14
    trainingData = dict(test2Gram, **test3Gram)

    print str(trainingData)
