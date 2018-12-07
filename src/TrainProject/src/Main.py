from WordConverter import WordConverterClass
from Train import TrainClass

import os, binascii
import gc
import datetime

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class MainClass:

    train_x = []
    test_x = []
    train_y = []
    test_y = []

    trainClass = TrainClass()
    wordConverter = WordConverterClass()

    def startup(self):
        print("train project started")
        self.wordConverter = WordConverterClass()
        self.train_x, self.test_x, self.train_y, self.test_y = self.wordConverter.creatTokenizers(
            'TrainProject\Data\Data.json')

        self.trainModel()

    def loadStartup(self, wordTokenizer, classTokenizer, weights, modelJSON):
        self.wordConverter = WordConverterClass()
        self.wordConverter.loadTokenizers(wordTokenizer, classTokenizer)
        self.trainClass.loadModel(modelJSON, weights)

        self.testModel()

    def trainModel(self):
        self.trainClass = TrainClass()
        self.trainClass.trainModel(self.train_x, self.test_x, self.train_y,
                                   self.test_y)
        self.testModel()

        #create beter test function
        #if test is completed and is above a threshold save the weights and tokenizers

    def testModel(self):
        self.getclass("Hello there ")
        self.getclass("Thanks, see you later")
        self.getclass("Could you tell me where LA402 is?")
        self.getclass("Is LD402 currently free?")
        self.getclass("I would like you to tell me where la402 is")
        self.getclass("Do you know where la1234 is?")

    def getclass(self, sentence):

        intention, certenty = self.trainClass.predictModel(
            self.wordConverter.convertSentenceToTokens(sentence),
            self.wordConverter)
        print("----------------------------------------------")
        print("Sentence is: {}".format(sentence))
        print("Intention: {}".format(intention))
        print("Certenty: {0:.2f}%".format(certenty * 100))
        print("----------------------------------------------")

    def saveNetwork(self, path):

        dateTimeNow = datetime.datetime.now()

        #id = dateTimeNow.strftime("%Y-%m-%d T %H;%M;%S")
        id = str(int(self.ticks(dateTimeNow)))

        modelJsonPath = path + id + ".modelJSON"
        weightsFilePath = path + id + ".weights"
        wordTokenizerPath = path + id + ".wordTokenizer"
        classTokenizerPath = path + id + ".classTokenizer"

        print("file path from weights = {}".format(weightsFilePath))
        print("file path from wordTokenzier = {}".format(wordTokenizerPath))
        print("file path from classTokenizer = {}".format(classTokenizerPath))
        self.trainClass.saveModel(modelJsonPath)
        self.trainClass.saveWeights(weightsFilePath)
        self.wordConverter.saveClassTokenizer(classTokenizerPath)
        self.wordConverter.saveWordTokenizer(wordTokenizerPath)
        gc.collect()
        print("model saved")

    def ticks(self, dt):
        return (dt - datetime.datetime(2018, 12, 1)).total_seconds()

    def loadNetwork(self, id):
        print("loading network")


main = MainClass()

# main.loadStartup("TrainProject\\Saves\\473909.wordTokenizer",
#                  "TrainProject\\Saves\\473909.classTokenizer",
#                  "TrainProject\\Saves\\473909.weights",
#                  "TrainProject\\Saves\\473909.modelJSON")

main.startup()
main.saveNetwork("TrainProject\\Saves\\")
