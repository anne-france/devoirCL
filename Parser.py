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
        
        
        self.fichiertest = "Dumas_test.txt"
       
        self.fichiertrain = "Dumas_train.txt"
        self.fichiertrainunk = "Dumas_train_unk.txt"
        self.fichiertest = "Dumas_test.txt"
        self.dicocount={}
        self.threeOccurencesCount={}
        self.dictUnigrame={}
        self.dictBigrame={}
        self.dictTrigrame={}
        self.dictProbUnigrame={}
        self.dictProbBigrame={}
        
    def prob_Add_One_Unigrams(self):
        nbre_token= len(self.dictUnigrame)
        total_words=0.0
        for count in self.dictUnigrame.itervalues():
            total_words=total_words+count
        
        for word,count in self.dictUnigrame.iteritems():
            self.dictProbUnigrame[word] = (count+1) / (total_words+nbre_token)
            
            
 
    def prob_Add_One_Bigrams(self):
        dicthistory={}
        #pas sure
        nbre_token= len(self.dictUnigrame)
        total_words=0.0
        for count in self.dictUnigrame.itervalues():
            total_words=total_words+count
       
       
        for word,count in self.dictBigrame.iteritems():
            counthistory=0.0
            wordhistory=word[0]
            counthistory=self.dictUnigrame.get((word[0],))
            counthistory= counthistory
            probahistory=self.dictProbUnigrame.get((word[0],))
            proba=((count+1.0) / (counthistory +nbre_token ))
            #proba= proba*probahistory
            print(str(counthistory))
            self.dictProbBigrame[word] =proba
             
    def verifProb(self):
        sumAllProb=0.0
        good=True
        for prob in self.dictProbUnigrame.itervalues():
            sumAllProb=sumAllProb+prob
        print("prob unigramme " +str(sumAllProb))
        if ( str(sumAllProb) != "1.0"):
            good=False 
        sumAllProb=0.0
        for prob in self.dictProbBigrame.itervalues():
            sumAllProb=sumAllProb+prob
        print("prob bigramme " +str(sumAllProb))
        if ( str(sumAllProb) != "1.0"):
            good=False 
        return good
    def mesgram(self) :
        fread = open(self.fichiertrainunk,"r")
        for l in fread: 
            malist=l.split()
            unigrams=self.__find_ngrams(malist, 1)
            self.__count_ngrams(unigrams,self.dictUnigrame)   
            bigrams=self.__find_ngrams(malist, 2)
            self.__count_ngrams(bigrams,self.dictBigrame) 
            trigrams=self.__find_ngrams(malist, 3)
            self.__count_ngrams(trigrams,self.dictTrigrame) 
            
        fread.close()   
        print(collections.Counter(self.dictUnigrame).most_common(20))
        print(collections.Counter(self.dictBigrame).most_common(20))
        print(collections.Counter(self.dictTrigrame).most_common(20))
       
        
    
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
        for v in self.dictBigrame.itervalues():
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
        for v in self.dictTrigrame.itervalues():
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
                self.threeOccurencesCount [k]=v
        #print(len(self.aumoinstrois))
        
    def standardinazionfile(self):
        fread = open(self.fichiertrain,"r")
        fwrite = open(self.fichiertrainunk,"w")
        regexexp = re.compile(r"(^\' \')|(^\'\s*)")
        for lines in fread:
            #retire "\n"
            lines.strip()
            line=lines.splitlines()      
            sentences=re.split(r'[?;/.!]', line[0])
           
            for sentence in sentences:
               
                sentence=sentence.lower()
                sentence = sentence.replace("'\"", '')
                sentence = sentence.replace('\"', '')         
                sentence = sentence.replace('`', '')
                sentence = sentence.replace(',', '')
                sentence = sentence.replace(':', '')
                sentence=sentence.strip()
               
                if (sentence != "" and sentence != '"' and sentence != "'" and sentence != " " ): 
                    
                       
                    sentence= re.sub(regexexp, '', sentence)

                    
                    words= sentence.split()
                    for word in words:
                        if (self.threeOccurencesCount.has_key(word)==False):
                            sentence = sentence.replace(word,"<UNK>")
      
                    sentence=sentence + " </s>\n"
                    #print(sentence)
                    fwrite.write(sentence)
                
            
        fwrite.close()
        fread.close()
            
       
    def count_wordfile(self):
        #ouverture du fichier
        file = open(self.fichiertrain,"r")
        for lines in file:
            lines.strip()
            line=lines.splitlines()
            words=line[0].split()           
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
                #print(word)
                if (word != ''):
                    if self.dicocount.has_key(word):                    
                        self.dicocount[word] = self.dicocount[word] +1
                    else :
                        self.dicocount[word]= 1
 
        print(len(self.dicocount))
        #les 20 mote les plus frequent
        print(collections.Counter(self.dicocount).most_common(20))
        #fermeture
        file.close()
       
        
        