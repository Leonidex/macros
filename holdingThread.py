"""
Custom thread class, used for performing button holding functions.
"""

import threading
import time

class holdingThread(threading.Thread):
    
    def __init__(self, actionFunc):
        threading.Thread.__init__(self)
        self.actionFunc = actionFunc

    def run(self):
        self.loopCondition = True
        while(self.loopCondition):
            self.actionFunc()
            time.sleep(0.001)

    def stopLoop(self):
        self.loopCondition = False
