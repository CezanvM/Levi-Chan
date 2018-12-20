#author: Cézan von Meijenfeldt
import time, threading


class ConversationHandlerClass:

    inConversation = False
    timerRestarted = False

    classroomInConversation = "kek"

    @staticmethod
    def conversationHandlerInit():
        ConversationHandlerClass.timerCallback()
        ConversationHandlerClass.inConversation = False

    @staticmethod
    def timerCallback():
        if ConversationHandlerClass.timerRestarted == False:
            if ConversationHandlerClass.inConversation == True:
                ConversationHandlerClass.endConversation()
                #end conversation
        else:
            ConversationHandlerClass.timerRestarted = False

        global t
        t = threading.Timer(20, ConversationHandlerClass.timerCallback)
        t.start()

    @staticmethod
    def setClassroom(classroom):
        ConversationHandlerClass.classroomInConversation = classroom

    @staticmethod
    def getClassroom():
        return ConversationHandlerClass.classroomInConversation

    @staticmethod
    def conversationInput():
        if ConversationHandlerClass.inConversation == False:
            print("Conversation started")
        t.cancel()
        ConversationHandlerClass.timerRestarted = True
        ConversationHandlerClass.timerCallback()
        ConversationHandlerClass.inConversation = True

    @staticmethod
    def endConversation():
        print("conversation ended room in conversation was {}".format(
            ConversationHandlerClass.classroomInConversation))
        ConversationHandlerClass.inConversation = False
        ConversationHandlerClass.classroomInConversation = ""
