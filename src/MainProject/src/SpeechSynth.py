from gtts import gTTS
from playsound import playsound

def SpeechSynthStartup():
    print("started SpeechSynth")
    SpeakSentence("Room LA15 is located on the first floor at the right side")


def SpeakSentence(sentence):
    print("speaking")
    speechOutput = gTTS(text=sentence, lang="en", slow=False)
    speechOutput.save("Output.mp3")
    playsound("Output.mp3")