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
    parser.statgram()
    parser.prob_Add_One_Unigrams()
    parser.prob_Add_One_Bigrams()
    print(parser.verifProb())