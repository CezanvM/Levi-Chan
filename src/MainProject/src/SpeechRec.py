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
            #microphone listining
            with self.mic as source:
                self.r.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.r.listen(source, 7)
                

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
        self.waitingOnAPI = False
