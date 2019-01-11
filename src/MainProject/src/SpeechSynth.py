#author: Lars van Dijk & Cézan von Meijenfeldt
#from UNKNOWN import gTTS
from espeak import espeak
#import pygame
#from tempfile import TemporaryFile
#import time
import os

class SpeechSynthCLass:
    def SpeakSentence(self, sentence):
        print("speaking")

	   # sf = TemporaryFile()
#        espeak.synth(sentence)
        stringToSpeak = ('flite -voice slt -t \"{}\"').format(sentence)
#        print(stringToSpeak)
        os.system(stringToSpeak)	    


#        while espeak.is_playing:
#	        print("in While")

#        speechOutput = gtts.tts.gTTS(text=sentence, lang="en", slow=False)
#        speechOutput.write_to_fp(sf)

#        pygame.mixer.init()
#        sf.seek(0)
#        pygame.mixer.music.load(sf.name)
#        pygame.mixer.music.play()

#        while pygame.mixer.music.get_busy():
#            time.sleep(0.5)

#        sf.close()
