from gtts import gTTS
from playsound import playsound
import os
import pygame
from tempfile import TemporaryFile
import time


class SpeechSynthCLass:
    def SpeakSentence(self, sentence):
        print("speaking")

        sf = TemporaryFile()

        speechOutput = gTTS(text=sentence, lang="en", slow=False)
        speechOutput.write_to_fp(sf)

        pygame.mixer.init()
        sf.seek(0)
        pygame.mixer.music.load(sf)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.5)

        sf.close()
