#author: Lars van Dijk
from InterpreterModule.QuestionInterpreter import QuestionInterpreterClass
import speech_recognition as sr
import pandas as pd
from InterpreterModule.ConversationHandler import ConversationHandlerClass

#import datetime


class SpeechRecClass:

    APIKey = "HOFLYUVHDMKRL6ZWGYM6UZ6I5B65A6P5"
    waitingOnAPI = False

    r = sr.Recognizer()
    mic = sr.Microphone()

    questionInterpreter = QuestionInterpreterClass()

    # timeBeforeCall = datetime.datetime.now
    # timeAfterCall = datetime.datetime.now
    r.energy_threshold = 4000

    def recLoop(self):
        while True:
            if ConversationHandlerClass.inConversation == False:
                input("Press Enter to continue...")

            self.r = sr.Recognizer()
            self.mic = sr.Microphone()
            #microphone listining
            isNotTimeout = False
            with self.mic as source:
                try:
                    print("listening")
                    audio = self.r.listen(
                        source, timeout=1, phrase_time_limit=5)
                    isNotTimeout = True
                except:
                    isNotTimeout = False
                    print("Timeout happend")

            print("Done listening")
            if isNotTimeout:
                if self.waitingOnAPI == False:
                    self.sendAudioToAPI(audio)

    def SpeechStartup(self):
        with self.mic as source:
            print("please wait, calibrating microphone....")
            self.r.adjust_for_ambient_noise(source, duration=5)
            self.r.dynamic_energy_threshold = True

    def sendAudioToAPI(self, sound):
        #self.timeBeforeCall = datetime.datetime.now

        self.waitingOnAPI = True
        #sending audio to API
        # TODO Check if working with bad english
        #sentence = self.r.recognize_wit(sound, self.APIKey)
        sentence = self.r.recognize_google(
            sound
        )  #used for basic audio testing, conversion testing done with WIT.ai
        if sentence != "":
            self.APICallback(sentence)
            ConversationHandlerClass.conversationInput()
        else:
            print("Nothing heard!")

    def APICallback(self, sentence):
        self.questionInterpreter.InterpretQuestion(sentence)
        print(sentence)
        self.waitingOnAPI = False
