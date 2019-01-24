#author: Cézan von Meijenfeldt

from InterpreterModule.QuestionInterpreter import QuestionInterpreterClass
from SpeechRec import SpeechRecClass
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
        self.startupNeuralNetwork()

        self.startupSpeechRec()

    def startupSpeechRec(self):
        speechClass = SpeechRecClass()
        speechClass.SpeechStartup()
        speechClass.recLoop()

    def startupNeuralNetwork(self):
        questionsInterpreterClass = QuestionInterpreterClass()
        questionsInterpreterClass.InterpreterStartup()

    def getWokringDirectory(self):
        pathList = os.path.split(sys.argv[0])
        print(pathList)


main = MainClass()
main.startup()