from InterpreterModule.QuestionInterpreter import QuestionInterpreterClass


def startup():
    print("welcome to Levi-chan")
    print("""
             _       _______ _     _ _              _______ _     _ _______ _______ 
            (_)     (_______|_)   (_ _)            (_______|_)   (_|_______|_______)
             _       _____   _     _ _   _____     _       _______ _______ _     _ 
            | |     |  ___) | |   | | |  (_____)   | |     |  ___  |  ___  | |   | |
            | |_____| |_____ \ \ / /| |            | |_____| |   | | |   | | |   | |
            |_______)_______) \___/ |_|             \______)_|   |_|_|   |_|_|   |_| """
          )

    questionsInterpreterClass = QuestionInterpreterClass()
    questionsInterpreterClass.InterpreterStartup()

    questionsInterpreterClass.InterpretQuestion("Hello there")
    questionsInterpreterClass.InterpretQuestion(
        "could you tell me where room la430 is located")


#SpeechRec.SpeechStartup()
#SpeechSynth.SpeechSynthStartup()

startup()