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
        self.dicoAtLeastThrre={}
        self.dicounigrame={}
        self.dicobigrame={}
        self.dicotrigrame={}
        
    def mesgram(self) :
        fread = open(self.fichiertrainunk,"r")
        for l in fread: 
            malist=l.split()
            unigrams=self.__find_ngrams(malist, 1)
            self.__count_ngrams(unigrams,self.dicounigrame)   
            bigrams=self.__find_ngrams(malist, 2)
            self.__count_ngrams(bigrams,self.dicobigrame) 
            trigrams=self.__find_ngrams(malist, 3)
            self.__count_ngrams(trigrams,self.dicotrigrame) 
            
        fread.close()   
        print(collections.Counter(self.dicounigrame).most_common(20))
        print(collections.Counter(self.dicobigrame).most_common(20))
        print(collections.Counter(self.dicotrigrame).most_common(20))
       
        
    
    def __find_ngrams(self,input_list, n):      
            return zip(*[input_list[i:] for i in range(n)])
        
    def __count_ngrams(self,gram_List, myDicoGram):   
        for gram in gram_List:
            if myDicoGram.has_key(gram):                    
                myDicoGram[gram] = myDicoGram[gram] +1
            else :
                myDicoGram[gram]= 1 
                  
    def statgram(self) :
        dicostatbi={}
        for v in self.dicobigrame.itervalues():
            if dicostatbi.has_key(v):                    
                dicostatbi[v] = dicostatbi[v] +1
            else :
                dicostatbi[v]= 1  
        sortedlist= sorted(dicostatbi.items(), key=lambda t: t[0])
        fwriterbi = open("stabitgrammebi.csv","w") 
        for entry in sortedlist:
            fwriterbi.write(str(entry[0]) +"," + str(entry[1])+"\n")       
             
        
        fwriterbi.close
        dicostattri={}
        for v in self.dicotrigrame.itervalues():
            if dicostattri.has_key(v):                    
                dicostattri[v] = dicostattri[v] +1
            else :
                dicostattri[v]= 1  
        sortedlist= sorted(dicostattri.items(), key=lambda t: t[0])
        fwritertri = open("stabitgrammetri.csv","w") 
        for entry in sortedlist:
            fwritertri.write(str(entry[0]) +"," + str(entry[1])+"\n")       
             
        
        fwritertri.close          
       
             
         
         
    def lexicon_aumoinstrois(self):          
        for k,v in self.dicocount.iteritems():
            if (v>=3):
                #print("mot " + k + " count= "+ str(v))
                self.dicoAtLeastThrre [k]=v
        #print(len(self.aumoinstrois))
        
    def standardinazionfile(self):
        fread = open(self.fichiertrain,"r")
        fwrite = open(self.fichiertrainunk,"w")
        for lignes in fread:
            #retire "\n"
            lignes.strip()
            ligne=lignes.splitlines()      
            sentences=re.split(r'[?;/.!]', ligne[0])
           
            for sentence in sentences:
                sentence=sentence.strip()
                sentence=sentence.lower()
                sentence = sentence.replace("'\"", '')
                sentence = sentence.replace('\"', '')         
                sentence = sentence.replace('`', '')
                sentence = sentence.replace(',', '')
                sentence = sentence.replace(':', '')
                if (sentence != "" and sentence != '"' and sentence != "'" and sentence != " " ):                  
                    words= sentence.split()
                    for word in words:
                        if (self.dicoAtLeastThrre.has_key(word)==False):
                            sentence = sentence.replace(word,"<UNK>")
      
                    sentence=sentence + " </s>\n"
                    #print(phrase)
                    fwrite.write(sentence)
                
            
        fwrite.close()
        fread.close()
            
       
    def count_wordfile(self):
        #ouverture du fichier
        fread = open(self.fichiertrain,"r")
        for lignes in fread:
                #retire "\n"
            lignes.strip()
            ligne=lignes.splitlines()
            words=ligne[0].split(" ")           
            for word in words:
                word = word.lower()
                word = word.replace('"', '', 4)
                word = word.replace('?', '')
                word = word.replace('.', '')
                word = word.replace('!', '')
                word = word.replace(';', '')
                word = word.replace(',', '')
                word = word.replace(':', '')
                word = word.replace(' ', '')
                if (word != ''):
                    if self.dicocount.has_key(word):                    
                        self.dicocount[word] = self.dicocount[word] +1
                    else :
                        self.dicocount[word]= 1
 
        print(len(self.dicocount))
        #les 20 mote les plus frequent
        print(collections.Counter(self.dicocount).most_common(20))
        #fermeture
        fread.close()
       
        
        