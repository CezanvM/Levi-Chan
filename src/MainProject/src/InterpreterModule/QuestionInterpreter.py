#author: Cézan von Meijenfeldt
from InterpreterModule.WordConverter import WordConverterClass
from InterpreterModule.NeuralNet import NeuralNetClass
from InterpreterModule.ConversationHandler import ConversationHandlerClass
from formulatingModule.createAnwser import CreateAnwserClass
from SpeechSynth import SpeechSynthCLass
from formulatingModule.ClassroomExtractor import ClassroomExtractorClass


class QuestionInterpreterClass:
    wordConverter = WordConverterClass()
    neuralNetClass = NeuralNetClass()
    createAnwserClass = CreateAnwserClass()
    speechSyntchClass = SpeechSynthCLass()
    classroomExtractorClass = ClassroomExtractorClass()

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

        ConversationHandlerClass.conversationHandlerInit()

    def InterpretQuestion(self, sentence):
        print("interpreting sentence")
        print(sentence)

        ConversationHandlerClass.conversationInput()

        intention, certenty = self.neuralNetClass.predictModel(
            self.wordConverter.convertSentenceToTokens(sentence),
            self.wordConverter)
        if certenty > 0.75:
            ConversationHandlerClass.addQuestionIntention(intention)
        else:
            intention, certenty = self.handleNotFinishedQuestion(sentence)

        print("----------------------------------------------")
        print("Sentence is: {}".format(sentence))
        print("Intention: {}".format(intention))
        print("Certenty: {0:.2f}%".format(certenty * 100))
        print("----------------------------------------------")
        print("----------------------------------------------")

        questionFinished, awnser = self.createAnwserClass.createAnwser(
            sentence, intention, certenty)
        ConversationHandlerClass.setQuestionFinished(questionFinished)

        print("Response is: {}".format(awnser))
        self.speechSyntchClass.SpeakSentence(awnser)
        print("----------------------------------------------")
        print("----------------------------------------------\n\n\n")
        # to awnser formulator

    def handleNotFinishedQuestion(self, sentence):
        #todo search if a earlyer question !finished
        if sentence != None:
            if ConversationHandlerClass.getQuestionFinished() == False:
                classroomValid, room = self.classroomExtractorClass.getClassRoom(
                    sentence)
                if classroomValid:
                    lastIntention = ConversationHandlerClass.getLastIntention()
                    newCertenty = 1
                    return lastIntention, newCertenty
