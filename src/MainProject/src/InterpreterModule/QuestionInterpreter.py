from InterpreterModule.WordConverter import WordConverterClass
from InterpreterModule.NeuralNet import NeuralNetClass


class QuestionInterpreterClass:
    wordConverter = WordConverterClass()
    neuralNetClass = NeuralNetClass()

    wordTokenizerPath = "MainProject\\Data\\NeuralNetSaves\\473909.wordTokenizer"
    classTokenizerPath = "MainProject\\Data\\NeuralNetSaves\\473909.classTokenizer"
    modelJsonPath = "MainProject\\Data\\NeuralNetSaves\\473909.modelJSON"
    weightsPath = "MainProject\\Data\\NeuralNetSaves\\473909.weights"

    def InterpreterStartup(self):
        print("starting Interpreter....")
        print("pulling weights from server logic here")
        self.wordConverter.loadTokenizers(self.wordTokenizerPath,
                                          self.classTokenizerPath)
        self.neuralNetClass.loadModel(self.modelJsonPath, self.weightsPath)

    def InterpretQuestion(self, sentence):
        intention, certenty = self.neuralNetClass.predictModel(
            self.wordConverter.convertSentenceToTokens(sentence),
            self.wordConverter)
        print("----------------------------------------------")
        print("Sentence is: {}".format(sentence))
        print("Intention: {}".format(intention))
        print("Certenty: {0:.2f}%".format(certenty * 100))
        print("----------------------------------------------")

    
