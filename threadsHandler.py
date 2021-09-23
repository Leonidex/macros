"""
Threads handler class, manages the threads that are in charge of performing the macro functions.
"""

from holdingThread import holdingThread
import threading

class threadsHandler():
    def __init__(self):
        self.holdThreads = {}
        self.buttonHeld = {}

    def createNewThread(self, actionFunc):
        thread = threading.Thread(target=actionFunc)
        return thread

    def createNewHoldThread(self, actionFunc):
        _holdingThread = holdingThread(actionFunc)
        return _holdingThread

    # def holdFunc(self, actionFunc, loopConditionFunc, buttonName):
    #     while(loopConditionFunc(None)):
    #         # print('holding!')
    #         actionFunc()

    def runPressAction(self, actionFunc):
        thread = self.createNewThread(actionFunc)
        thread.start()
    
    def runHoldAction(self, actionFunc, buttonName):
        self.buttonHeld[buttonName] = True
        print('holding')
        thread = self.createNewHoldThread(actionFunc)
        self.holdThreads[buttonName] = thread
        thread.start()

    def runReleaseAction(self, actionFunc, buttonName):
        self.buttonHeld[buttonName] = False
        self.holdThreads[buttonName].stopLoop()
        print('released')
        thread = self.createNewThread(actionFunc)
        thread.start()