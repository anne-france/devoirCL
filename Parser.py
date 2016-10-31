import re

class Parser:

    def __init__(self, fileName):
        self.fileName = fileName

    def getLineWordList(self, line):
        lineWordsList = re.split(r'\(?\)?\,?\"?\`?-?\:?\;?(\!?)(\??)(\.?)\s?', line.lower())
        listLength = lineWordsList.__len__()
        word = 0
        while word < listLength:
            if lineWordsList[word] == '':
                lineWordsList.remove('')
                word -= 1
                listLength -= 1
            word += 1
        return lineWordsList

    def getListOfWordsInFile(self):
        file = open(self.fileName,"r")
        wordListOfFile = []
        for line in file:
            wordListOfFile = wordListOfFile + self.getLineWordList(line)
        file.close()

        return self.parsePunctuation(wordListOfFile)

    def getUnigram(self):
        uniGram = {}
        file = open(self.fileName,"r")
        for line in file:
            lineWordList = self.parsePunctuation(self.getLineWordList(line))
            word = 0
            while word < lineWordList.__len__():
                if uniGram.has_key(lineWordList[word]):
                    uniGram[lineWordList[word]] += 1
                else:
                    uniGram[lineWordList[word]] = 1
                word += 1
        return uniGram

    def getNGram(self, n, uniGram):
        nGram = {}
        wordsFromPreviousLine = []
        file = open(self.fileName,"r")
        for line in file:
            lineWordList = self.parsePunctuation(self.getLineWordList(line))
            word = 0
            while word < lineWordList.__len__() - (n - 1):
                lexicon = ""
                if wordsFromPreviousLine.__len__() != 0:
                    for previousWords in wordsFromPreviousLine:
                        if uniGram.has_key(previousWords):
                            lexicon += previousWords + " "
                        else:
                            lexicon += "<UNK>" + " "
                    wordsFromPreviousLine.pop(0)
                    wordLineCount = 0
                    while lexicon[:-1].split(" ").__len__() < n:
                        if uniGram.has_key(lineWordList[wordLineCount]):
                            lexicon += lineWordList[wordLineCount] + " "
                        else:
                            lexicon += "<UNK>" + " "
                        wordLineCount += 1
                    if wordsFromPreviousLine.__len__() == 0:
                        word = -1
                else:
                    for wordInLexicon in range(0, n):
                        if uniGram.has_key(lineWordList[word + wordInLexicon]):
                            lexicon += lineWordList[word + wordInLexicon] + " "
                        else:
                            lexicon += "<UNK>" + " "
                lexicon = lexicon[:-1]
                if nGram.has_key(lexicon):
                    nGram[lexicon] += 1
                else:
                    nGram[lexicon] = 1
                word += 1
            for words in range(lineWordList.__len__() - (n - 1), lineWordList.__len__()):
                wordsFromPreviousLine.append(lineWordList[words])
        return nGram

    def parsePunctuation(self, wordList):
        for word in range(0, wordList.__len__()):
            if wordList[word] == "!" or wordList[word] == "." or wordList[word] == "?":
                wordList[word] = "</s>"
        return wordList
