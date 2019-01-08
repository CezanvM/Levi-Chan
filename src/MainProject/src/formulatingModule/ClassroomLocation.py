#author: Cézan von Meijenfeldt

from formulatingModule.ClassroomExtractor import ClassroomExtractorClass


class ClassroomLocationClass:

    classroomExtractorClass = ClassroomExtractorClass()

    def getRoute(self, sentence):
        classroomFound = False
        print("Getting route to classroom")
        valid, classroom = self.classroomExtractorClass.getClassRoom(sentence)
        print(classroom)
        if valid:  # small convertion for the tts
            classroomFound = True
            if "la" in classroom:
                speechClassroom = classroom.replace("la", "L A ", 1)
            elif "ld" in classroom:
                speechClassroom = classroom.replace("ld", "L D ", 1)
            return classroomFound, speechClassroom

        else:
            print("classroom not found")
            #handle classroom not found ask for classroom
            return classroomFound, "classroom not found"

    def startupClassroomLocation(self, configFile):
            



class Building:
   floors = []
   sentence = ""

class Floor:
    rooms = []
    sentence = ""

class Classroom:
    sentence = ""