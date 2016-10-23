'''
Created on 21 oct. 2016

@author: anne-francevanswieten
'''
import operator
import collections
class Parser:
    '''
    classdocs
    '''


    def __init__(self):
        
        self.fichiertrain = "Dumas_train.txt"
        self.dicocount={}
        self.aumoinstrois={}
        
    def lexicon_aumoinstrois(self): 
         
        for k,v in self.dicocount.iteritems():
            if (v>=3):
                print("mot " + k + " count= "+ str(v))
                self.aumoinstrois [k]=v
       
        
    def count_wordfile(self):
        #ouverture du fichier
        f = open(self.fichiertrain,"r")
    
        for l in f:
           
            #retire "\n"
            l.strip()
            w=l.splitlines()
            #print(w,len(w))
            mots=w[0].split(" ")
            
           
            for mot in mots:
                #print(mot,len(mot))
                mot=mot.lower()
                mot = mot.replace('"', '', 2)
                mot = mot.replace('?', '')
                mot = mot.replace('.', '')
                mot = mot.replace('!', '')
                mot = mot.replace(';', '')
                mot = mot.replace(',', '')
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
        #les 20 mote les plus frequents
        
        print(collections.Counter(self.dicocount).most_common(20))
        
        print("\n")
       
        #fermeture
        f.close()
       
        
        