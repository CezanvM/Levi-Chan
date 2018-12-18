#author: Cézan von Meijenfeldt
import time, threading


class ConversationHandlerClass:

    inConversation = False
    timerRestarted = False

    classroomInConversation = ""

    def conversationHandlerInit(self):
        self.timerCallback()
        self.inConversation = False

    def timerCallback(self):
        if self.timerRestarted == False:
            if self.inConversation == True:
                self.endConversation()
                #end conversation
        else:
            self.timerRestarted = False

        global t
        t = threading.Timer(15, self.timerCallback)
        t.start()

    def setClassroom(self, classroom):
        self.classroomInConversation = classroom

    def conversationInput(self):
        if self.inConversation == False:
            print("Conversation started")
        t.cancel()
        self.timerRestarted = True
        self.timerCallback()
        self.inConversation = True

    def endConversation(self):
        print("conversation ended")
        self.inConversation = False
        self.classroomInConversation = ""
