import QuestionInterpreter

waitingOnAPI = False


def recLoop():
    print("listering")
    if waitingOnAPI == False:
        sendAudioToAPI()


def SpeechStartup():
    print("speech started")
    recLoop()


def sendAudioToAPI():
    APICallback("this is a sentence")


def APICallback(sentence):
    QuestionInterpreter.InterpretQuestion(sentence)