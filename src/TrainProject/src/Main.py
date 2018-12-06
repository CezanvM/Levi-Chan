from WordConverter import WordConverterClass
from Train import TrainClass
import pickle
import os, binascii
import gc
import datetime


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
            'Data\Data.json')

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

        # path = path + "{}\\".format(dateTimeNow.strftime("%Y-%m-%dT%H;%M;%S"))
        # os.makedirs(path)

        # id = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
        id = dateTimeNow.strftime("%Y-%m-%d T %H;%M;%S")
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

    def loadNetwork(self, id):
        print("loading network")


main = MainClass()

main.loadStartup("Saves\\2018-12-04 T 10;02;32.wordTokenizer",
                 "Saves\\2018-12-04 T 10;02;32.classTokenizer",
                 "Saves\\2018-12-04 T 10;02;32.weights",
                 "Saves\\2018-12-04 T 10;02;32.modelJSON")

# main.startup()
# main.saveNetwork("Saves\\")
