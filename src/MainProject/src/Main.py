from InterpreterModule.QuestionInterpreter import QuestionInterpreterClass
import SpeechRec
import SpeechSynth
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class MainClass:
    workingDirectory = ""

    def startup(self):
        print("welcome to Levi-chan")
        print("""
               _       _______ _     _ _              _______ _     _ _______ _______ 
              (_)     (_______|_)   (_ _)            (_______|_)   (_|_______|_______)
               _       _____   _     _ _   _____     _       _______ _______ _     _ 
              | |     |  ___) | |   | | |  (_____)   | |     |  ___  |  ___  | |   | |
              | |_____| |_____ \ \ / /| |            | |_____| |   | | |   | | |   | |
              |_______)_______) \___/ |_|             \______)_|   |_|_|   |_|_|   |_| \n\n"""
              )
        #self.getWokringDirectory()
        SpeechSynth.SpeechSynthStartup()
        #SpeechRec.SpeechStartup()
        #self.startupNeuralNetwork()
'''  
    def startupNeuralNetwork(self):
        questionsInterpreterClass = QuestionInterpreterClass()
        questionsInterpreterClass.InterpreterStartup()

        questionsInterpreterClass.InterpretQuestion("Hello there")
        questionsInterpreterClass.InterpretQuestion(
            "could you tell me where room la430 is located")
        questionsInterpreterClass.InterpretQuestion("How are you doing today")

    def getWokringDirectory(self):
        pathList = os.path.split(sys.argv[0])
        print(pathList)


#SpeechRec.SpeechStartup()
#SpeechSynth.SpeechSynthStartup()

main = MainClass()
main.startup()