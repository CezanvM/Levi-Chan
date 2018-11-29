from WordConverter import WordConverterClass
from Train import TrainClass


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
        self.train_x, self.test_x, self.train_y, self.test_y = self.wordConverter.importData(
            'Data\Data.json')

        self.trainModel()

    def trainModel(self):
        self.trainClass = TrainClass()
        self.trainClass.trainModel(self.train_x, self.test_x, self.train_y,
                                   self.test_y)
        self.testModel()

    def testModel(self):
        self.getclass("Hello there")
        self.getclass("thanks, see you later")
        self.getclass("could you tell me where LA402 is?")
        self.getclass("is LD402 currently free?")

    def getclass(self, sentence):

        intention, certenty = self.trainClass.predictModel(
            self.wordConverter.convertSentenceToTokens(sentence),
            self.wordConverter)
        print("----------------------------------------------")
        print("Sentence is: {}".format(sentence))
        print("Intention: {}".format(intention))
        print("Certenty: {0:.2f}%".format(certenty * 100))
        print("----------------------------------------------")


main = MainClass()
main.startup()
