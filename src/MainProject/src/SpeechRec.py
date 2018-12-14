from InterpreterModule.QuestionInterpreter import QuestionInterpreterClass

import speech_recognition as sr
import pandas as pd
import datetime
import json
from playsound import playsound

questionsInterpreterClass = QuestionInterpreterClass()

APIKey = "HOFLYUVHDMKRL6ZWGYM6UZ6I5B65A6P5"
waitingOnAPI = False

r = sr.Recognizer()
mic = sr.Microphone()

def recLoop():
	print("Listening")
	#microphone listining
	with mic as source:
		r.adjust_for_ambient_noise(source, duration=0.5)
		audio = r.listen(source)

	print("Done listening")

	if waitingOnAPI == False:
		sendAudioToAPI(audio)
		
def SpeechStartup():
	recLoop()
	
def sendAudioToAPI(sound):
	waitingOnAPI = True
	#sending audio to API
	# TODO Check if working with bad english
	sentence =  r.recognize_wit(sound, APIKey)
	#sentence =  r.recognize_google(sound) #used for basic audio testing, conversion testing done with WIT.ai
	APICallback(sentence)


def APICallback(sentence):
	print(sentence)
	#questionsInterpreterClass.InterpretQuestion(sentence)
	waitingOnAPI = False
