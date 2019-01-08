#author: Cézan von Meijenfeldt
from formulatingModule.ClassroomExtractor import ClassroomExtractorClass


class ClassroomOccupiedClass:

    classroomExtractorClass = ClassroomExtractorClass()

    def getAvailibilty(self, sentence):
        classroomFound = False
        print("Getting availibilty")
        valid, classroom = self.classroomExtractorClass.getClassRoom(sentence)
        if valid:
            classroomFound = True
            # small convertion for the tts
            if "la" in classroom:
                speechClassroom = classroom.replace("la", "L A ", 1)
            elif "ld" in classroom:
                speechClassroom = classroom.replace("ld", "L D ", 1)
            return classroomFound, speechClassroom

        else:
            print("classroom not found")
            return classroomFound, "classroom not found"
