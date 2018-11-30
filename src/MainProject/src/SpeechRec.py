import QuestionInterpreter

import speech_recognition as sr
import pandas as pd
import datetime
import json
from playsound import playsound
print(sr.__version__)

APIKey = "HOFLYUVHDMKRL6ZWGYM6UZ6I5B65A6P5"
waitingOnAPI = False
#soundfile = "harvard.wav"
soundfile = "jackhammer.wav" #currently not imported since its unnesesary when audo recording works

r = sr.Recognizer()

def recLoop():
	print("listering")
	# TODO Actual audio recording
	audio = sr.AudioFile(soundfile)
	if waitingOnAPI == False:
		sendAudioToAPI(audio)


def SpeechStartup():
    print("speech started")
    recLoop()


def sendAudioToAPI(sound):
	waitingOnAPI = True

	#converting audio to correct type
	with sound as source:
		r.adjust_for_ambient_noise(source, duration=0.5)
		audio = r.record(source, duration=4)
	
	#sending audio to API
	sentence =  r.recognize_wit(audio, APIKey)
	APICallback(sentence)


def APICallback(sentence):
	QuestionInterpreter.InterpretQuestion(sentence)
	waitingOnAPI = False
