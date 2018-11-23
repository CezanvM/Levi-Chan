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

    def testModel(self):
        test = []
        test.append("hello")
        print(self.wordConverter.convertSentenceToTokens(test))


main = MainClass()
main.startup()
