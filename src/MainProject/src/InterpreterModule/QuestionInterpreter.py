#author: Cézan von Meijenfeldt
from InterpreterModule.WordConverter import WordConverterClass
from InterpreterModule.NeuralNet import NeuralNetClass


class QuestionInterpreterClass:
    wordConverter = WordConverterClass()
    neuralNetClass = NeuralNetClass()

    wordTokenizerPath = "MainProject\\Data\\NeuralNetSaves\\558613.wordTokenizer"
    classTokenizerPath = "MainProject\\Data\\NeuralNetSaves\\558613.classTokenizer"
    modelJsonPath = "MainProject\\Data\\NeuralNetSaves\\558613.modelJSON"
    weightsPath = "MainProject\\Data\\NeuralNetSaves\\558613.weights"

    def InterpreterStartup(self):
        print("starting Interpreter....")
        print("pulling weights from server logic here")
        self.wordConverter.loadTokenizers(self.wordTokenizerPath,
                                          self.classTokenizerPath)
        self.neuralNetClass.loadModel(self.modelJsonPath, self.weightsPath)

    def InterpretQuestion(self, sentence):
        print("interpreting sentence")
        intention, certenty = self.neuralNetClass.predictModel(
            self.wordConverter.convertSentenceToTokens(sentence),
            self.wordConverter)
        print("----------------------------------------------")
        print("Sentence is: {}".format(sentence))
        print("Intention: {}".format(intention))
        print("Certenty: {0:.2f}%".format(certenty * 100)
        print("----------------------------------------------")


        # to awnser formulator
