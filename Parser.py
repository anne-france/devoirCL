'''
Created on 21 oct. 2016

@author: anne-francevanswieten
'''
import operator
import collections
import re
class Parser:
    '''
    classdocs
    '''


    def __init__(self):
        
        self.fichiertrain = "Dumas_train.txt"
        self.fichiertrainunk = "Dumas_train_unk.txt"
        self.fichiertest = "Dumas_test.txt"
        self.dicocount={}
        self.threeOccurencesCount={}
        self.dictUnigrame={}
        self.dictBigrame={}
        self.dictTrigrame={}
        
    def mesgram(self) :
        file = open(self.fichiertrainunk,"r")
        for line in file:
            malist=line.split()
            unigrams=self.__find_ngrams(malist, 1)
            for unigram in unigrams:
                
        
                if self.dictUnigrame.has_key(unigram):
                    self.dictUnigrame[unigram] = self.dictUnigrame[unigram] + 1
                else :
                    self.dictUnigrame[unigram]= 1
            bigrams=self.__find_ngrams(malist, 2)
            for bigram in bigrams:
                
        
                if self.dictBigrame.has_key(bigram):
                    self.dictBigrame[bigram] = self.dictBigrame[bigram] + 1
                else :
                    self.dictBigrame[bigram]= 1
            trigrams=self.__find_ngrams(malist, 3)
            for trigram in trigrams:
                
        
                if self.dictTrigrame.has_key(trigram):
                    self.dictTrigrame[trigram] = self.dictTrigrame[trigram] + 1
                else :
                    self.dictTrigrame[trigram]= 1
            
           
        print(collections.Counter(self.dictUnigrame).most_common(20))
        print(collections.Counter(self.dictBigrame).most_common(20))
        print(collections.Counter(self.dictTrigrame).most_common(20))
       
        
    def __my_private_method(self):
        pass

    def __find_ngrams(self,input_list, n):
      
            return zip(*[input_list[i:] for i in range(n)])
        

        
    def lexicon_aumoinstrois(self): 
         
        for k,v in self.dicocount.iteritems():
            if (v>=3):
                #print("mot " + k + " count= "+ str(v))
                self.threeOccurencesCount [k]=v
        print(len(self.threeOccurencesCount))
        
    def standardinazionfile(self):
        file = open(self.fichiertrain,"r")
        fwrite = open(self.fichiertrainunk,"w")
        for line in file:
            #retire "\n"
            line.strip()
            w=line.splitlines()
            #print(w,len(w))
            
            
            phrases=re.split(r'[?;/.!]', w[0])
           
           
            #phrases=w[0].split(".")
            for phrase in phrases:
                phrase=phrase.strip()
            
                phrase=phrase.lower()
                phrase = phrase.replace("'\"", '')
               
                phrase = phrase.replace('\"', '')
               
               #phrase= phrase.replace("\\", "\\\\")
                phrase = phrase.replace('`', '')
                phrase = phrase.replace(',', '')
                phrase = phrase.replace(':', '')
               
                
                  
                

                
                if (phrase != "" and phrase != '"' and phrase != "'" and phrase != " " ):
                    
                    mots= phrase.split()
                    for mot in mots:
                        if (self.threeOccurencesCount.get(mot)==None):
                            phrase = phrase.replace(mot, '<UNK>')

                           
                    phrase="<s> " + phrase + " </s>\n"
                    #print(phrase)
                    fwrite.write(phrase)
                
            
        fwrite.close()
        file.close()
            
        
        
       
        
    def count_wordfile(self):
        #ouverture du fichier
        file = open(self.fichiertrain,"r")
    
        for line in file:
           
            #retire "\n"
            line.strip()
            w=line.splitlines()
            #print(w,len(w))
            mots=w[0].split(" ")
            
           
            for mot in mots:
                #print(mot,len(mot))
                mot=mot.lower()
                mot = mot.replace('"', '', 4)
                mot = mot.replace('?', '')
                mot = mot.replace('.', '')
                mot = mot.replace('!', '')
                mot = mot.replace(';', '')
                mot = mot.replace(',', '')
                mot = mot.replace(':', '')
                mot = mot.replace(' ', '')
                if (mot != ''):
                    if self.dicocount.has_key(mot):                    
                        self.dicocount[mot] = self.dicocount[mot] +1
                    else :
                        self.dicocount[mot]= 1
         
        #for key, value in self.dicocount.iteritems():
            #print key, value      
        # trier sur la valeur plus bessoin
        #dicotrier= sorted(self.dicocount.iteritems(), reverse=True, key=operator.itemgetter(1))
        #
        print(len(self.dicocount))
        #les 20 mote les plus frequents
        
        print(collections.Counter(self.dicocount).most_common(20))
        
        print("\n")
       
        #fermeture
        file.close()
       
        
        