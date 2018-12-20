#author: Cézan von Meijenfeldt
from formulatingModule.ClassroomLocation import ClassroomLocationClass
from formulatingModule.ClassroomOccupied import ClassroomOccupiedClass


class CreateAnwserClass:

    classroomLocationClass = ClassroomLocationClass()
    classroomOccupiedClass = ClassroomOccupiedClass()

    def createAnwser(self, sentence, intention, certenty):
        print("Creating anwser")
        if certenty > 0.75:
            print("I understand what you said")

            return self.handleSureResponse(intention, sentence)

        else:
            return self.unsureResponse()

    def unsureResponse(self):
        return "Sorry could you repeat your last question"

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
        return "Hello there, what can i do for you?"

    def handleGrateful(self, sentence):
        return "You're welcome"

    def handleGoodbye(self, sentence):
        return "Goodbye!"

    def handleClassroomLocation(self, sentence):
        classroom = self.classroomLocationClass.getRoute(sentence)

        #format classroom name from la120 to L A 120 for tts

        return "you asked a question about the location of {} ".format(
            classroom)

    def handleClassroomOccupied(self, sentence):
        classroom = self.classroomOccupiedClass.getAvailibilty(sentence)

        return "you asked a question about the availibilty of {}".format(
            classroom)
