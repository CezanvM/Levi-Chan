import SpeechRec
import QuestionInterpreter
import SpeechSynth


def startup():
    print("welcome to Levi-chan")
    print("""
             _       _______ _     _ _              _______ _     _ _______ _______ 
            (_)     (_______|_)   (_) |            (_______|_)   (_|_______|_______)
             _       _____   _     _| |   _____     _       _______ _______ _     _ 
            | |     |  ___) | |   | | |  (_____)   | |     |  ___  |  ___  | |   | |
            | |_____| |_____ \ \ / /| |            | |_____| |   | | |   | | |   | |
            |_______)_______) \___/ |_|             \______)_|   |_|_|   |_|_|   |_| """
          )

    QuestionInterpreter.InterpreterStartup()
    SpeechRec.SpeechStartup()
    SpeechSynth.SpeechSynthStartup()


startup()