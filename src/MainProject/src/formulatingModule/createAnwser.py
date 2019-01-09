#author: Cézan von Meijenfeldt
from formulatingModule.ClassroomLocation import ClassroomLocationClass
from formulatingModule.ClassroomOccupied import ClassroomOccupiedClass


class CreateAnwserClass:

    classroomLocationClass = ClassroomLocationClass()
    classroomOccupiedClass = ClassroomOccupiedClass()
    questionFinished = True

    def createAnwser(self, sentence, intention, certenty):
        print("Creating anwser")
        if certenty > 0.75:
            print("I understand what you said")

            return self.handleSureResponse(intention, sentence)

        else:
            return self.unsureResponse()

    def unsureResponse(self):
        questionFinished = True
        return questionFinished, "Sorry could you repeat your last question"

    def handleSureResponse(self, intention, sentence):
        if intention == "greeting":
            return self.handleGreeting(sentence)
        elif intention == "grateful":
            return self.handleGrateful(sentence)
        elif intention == "goodbye":
            return self.handleGoodbye(sentence)
        elif intention == "classroomlocation":
            return self.handleClassroomLocation(sentence)
        elif intention == "classroomoccupied":
            return self.handleClassroomOccupied(sentence)

    def handleGreeting(self, sentence):
        # good morning, good afternoon depending on time
        questionFinished = True
        return questionFinished, "Hello there, what can i do for you?"

    def handleGrateful(self, sentence):
        questionFinished = True
        return questionFinished, "You're welcome"

    def handleGoodbye(self, sentence):
        questionFinished = True
        return questionFinished, "Goodbye!"

    def handleClassroomLocation(self, sentence):
        classroomFound, classroom = self.classroomLocationClass.getRoute(
            sentence)

        #format classroom name from la120 to L A 120 for tts
        if classroomFound:
            questionFinished = True
            return questionFinished, classroom
        else:
            questionFinished = False
            return questionFinished, "Sorry could you repeat the classroom you are looking for."
            #todo add classroom extractor to low pecentage sentences

    def handleClassroomOccupied(self, sentence):
        classroomFound, classroom = self.classroomOccupiedClass.getAvailibilty(
            sentence)

        if classroomFound:
            questionFinished = True
            return questionFinished, "you asked a question about the availibilty of {}".format(
                classroom)
        else:
            questionFinished = False
            return questionFinished, "Sorry could you repeat the classroom you are looking for."
            #todo add classroom extractor to low pecentage sentences
