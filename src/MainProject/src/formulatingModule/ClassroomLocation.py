#author: Cézan von Meijenfeldt

import json
from formulatingModule.ClassroomExtractor import ClassroomExtractorClass


class ClassroomLocationClass:

    classroomExtractorClass = ClassroomExtractorClass()

    def getRoute(self, sentence):
       classroomFound = False
        valid, classroom = self.classroomExtractorClass.getClassRoom(sentence)
        
        if valid:  # small convertion for the tts
            print("Getting route to classroom")
            if "la" in classroom:
                speechClassroom = classroom.replace("la", "L A ", 1)
                floor = int(speechClassroom[4:5])
                room = speechClassroom[5:]
                LAdata = json.loads(open('MainProject\\Data\\BuildingConfig\\LAConfigFile.json').read())
                Outputsentence = 'You asked for a route to room ' + speechClassroom + '. '
                Outputsentence = Outputsentence + LAdata['Floors'][floor]['Location']
                for i in LAdata['Floors'][floor]['ClassRooms']:
                    if i['Room'] == room :
                        Outputsentence = Outputsentence + i['Location']
                        classroomFound = True
                        break

                return classroomFound, Outputsentence
            elif "ld" in classroom:
                classroomFound = False
                speechClassroom = classroom.replace("ld", "L D ", 1)
            return FalclassroomFoundse, Outputsentence

        else:
            print("classroom not found")
            classroomFound = False
            #handle classroom not found ask for classroom
            return classroomFound, "classroom not found"

    #def startupClassroomLocation(self, configFile):
