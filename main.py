from Parser import Parser
import cProfile
from modelTrainer import ModelTrainer
from modelTester import ModelTester

if __name__ == '__main__':
    trainingParser = Parser("Dumas_train.txt")
    testParser = Parser("Dumas_test.txt")
    modelTrainer = ModelTrainer(trainingParser)
    modelTester = ModelTester(testParser)

    #Training
    # uniGram = modelTrainer.train(1)
    # biGram = modelTrainer.train(2)
    triGram = modelTrainer.train(3)

    #Count
    #uniGram.printLexiconCount()
    #biGram.printLexiconCount()
    #triGram.printLexiconCount()

    #20 more frequent
    #uniGram.printTwentyMoreFrequentLexicon()
    #biGram.printTwentyMoreFrequentLexicon()
    triGram.printTwentyMoreFrequentLexicon()

    #Process perplexity
    print "Laplace perplexity : " + str(modelTester.getPerplexity(triGram, "laplace")) + " on " + str(triGram.getLexiconCount()) + " lexicon type"
    print "Bayesian perplexity : " + str(modelTester.getPerplexity(triGram, "backoff")) + " on " + str(triGram.getLexiconCount()) + " lexicon type"
    
    #Excel
    #biGram.statCvs();
    #triGram.statCvs();

    #Shannon game
    triGram.playShannonGame("indeed you are right")