#author: Lars van Dijk
from InterpreterModule.QuestionInterpreter import QuestionInterpreterClass
import speech_recognition as sr
import pandas as pd
import datetime
import json
from playsound import playsound


class SpeechRecClass:

    APIKey = "HOFLYUVHDMKRL6ZWGYM6UZ6I5B65A6P5"
    waitingOnAPI = False

    r = sr.Recognizer()
    mic = sr.Microphone()

    questionInterpreter = QuestionInterpreterClass()

    def recLoop(self):
        while True:
            print("Listening")
            self.r = sr.Recognizer()
            self.mic = sr.Microphone()
            #microphone listining
            with self.mic as source:
                print("voor")
                self.r.adjust_for_ambient_noise(source, duration=0.5)
                print("achter")
                audio = self.r.listen(source, 2, phrase_time_limit=3)
                print("eind")

            print("Done listening")

            if self.waitingOnAPI == False:
                self.sendAudioToAPI(audio)

    def SpeechStartup(self):
        self.recLoop()

    def sendAudioToAPI(self, sound):
        self.waitingOnAPI = True
        #sending audio to API
        # TODO Check if working with bad english
        sentence = self.r.recognize_wit(sound, self.APIKey)
        #sentence =  r.recognize_google(sound) #used for basic audio testing, conversion testing done with WIT.ai
        self.APICallback(sentence)

    def APICallback(self, sentence):
        self.questionInterpreter.InterpretQuestion(sentence)
        print(sentence)
        self.waitingOnAPI = False
