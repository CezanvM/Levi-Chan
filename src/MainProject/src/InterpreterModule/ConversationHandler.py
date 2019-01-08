#author: Cézan von Meijenfeldt
import time, threading


class ConversationHandlerClass:

    inConversation = False
    timerRestarted = False

    classroomInConversation = None
    questionFinished = True
    intentions = []

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
    def setQuestionFinished(isFinished):
        ConversationHandlerClass.questionFinished = isFinished

    @staticmethod
    def getLastIntention():
        intentionList = ConversationHandlerClass.intentions
        return intentionList[len(intentionList) - 1]

    @staticmethod
    def getQuestionFinished():
        return ConversationHandlerClass.questionFinished

    @staticmethod
    def addQuestionIntention(Intention):
        ConversationHandlerClass.intentions.append(Intention)

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
        print("conversation ended, the classroom in the conversation was {}".
              format(ConversationHandlerClass.classroomInConversation))
        ConversationHandlerClass.inConversation = False
        ConversationHandlerClass.classroomInConversation = None
        ConversationHandlerClass.intentions.clear()
