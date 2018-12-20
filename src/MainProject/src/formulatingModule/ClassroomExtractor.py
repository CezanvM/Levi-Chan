#author: Cézan von Meijenfeldt
from InterpreterModule.ConversationHandler import ConversationHandlerClass


class ClassroomExtractorClass:
    def getClassRoom(self, sentence):
        print("retreiving classroom")
        sentence = sentence.lower()
        words = sentence.split()
        room = ""
        validClass = False

        for w in words:
            if w == 'la':
                room = self.handleRoomLA(words[words.index(w) + 1])
                validClass = True
                break
            if w == 'ld':
                room = self.handleRoomLD()
                validClass = True
                break

        valid, rooms = self.deeperSearch(words)
        if valid:
            room = rooms[0]
            validClass = True

        #@todo search better for classrooms like la120 instead of la 120
        #@todo if not found ask conversation handler about the classroom

        if validClass:
            ConversationHandlerClass.setClassroom(room)

        else:
            room = ConversationHandlerClass.getClassroom()
            if room != "":
                validClass = True

        return validClass, room

    def handleRoomLA(self, number):
        classroom = "la{}".format(number)
        ConversationHandlerClass.setClassroom(classroom)
        print("found classroom is {} ".format(classroom))
        return classroom

    def handleRoomLD(self, number):
        classroom = "ld{}".format(number)
        ConversationHandlerClass.setClassroom(classroom)
        print("found classroom is {} ".format(classroom))
        return classroom

    def deeperSearch(self, words):
        potentialRooms = []
        deepSearchValid = False
        for w in words:
            if "la" in w:
                valid, value = self.extractNumber(w)
                if valid:
                    potentialRooms.append("la{}".format(value))
                    deepSearchValid = True
            elif "ld" in w:
                valid, value = self.extractNumber(w)
                if valid:
                    potentialRooms.append("ld {}".format(value))
                    deepSearchValid = True

        return deepSearchValid, potentialRooms

    def extractNumber(self, word):
        digit = ""
        letters = list(word)
        found = False
        for l in letters:
            if l.isdigit():
                digit += "{}".format(l)
                found = True
            elif (found):
                return found, digit

        return found, digit
