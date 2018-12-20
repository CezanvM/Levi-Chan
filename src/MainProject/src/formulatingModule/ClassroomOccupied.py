#author: Cézan von Meijenfeldt
from formulatingModule.ClassroomExtractor import ClassroomExtractorClass


class ClassroomOccupiedClass:

    classroomExtractorClass = ClassroomExtractorClass()

    def getAvailibilty(self, sentence):
        print("Getting availibilty")
        valid, classroom = self.classroomExtractorClass.getClassRoom(sentence)
        if valid:  # small convertion for the tts
            if "la" in classroom:
                speechClassroom = classroom.replace("la", "L A ", 1)
            elif "ld" in classroom:
                speechClassroom = classroom.replace("ld", "L D ", 1)
            return speechClassroom

        else:
            print("classroom not found")
