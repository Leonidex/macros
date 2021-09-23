"""
Macros handling class, calls for specific macros for each button press, hold and release.
Designed specificaly for Logitech G502 Mouse.
"""

from threadsHandler import threadsHandler
from actions import button10Actions, button11Actions, button12Actions, button13Actions, button14Actions, button15Actions
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KBController

class macrosHandler():

    def __init__(self):
        self.threadsHandler = threadsHandler()
        self.buttons = {
            'button10':False,
            'button11':False,
            'button12':False,
            'button13':False,
            'button14':False,
            'button15':False
        }
        mouseController = MouseController()
        keyboardController = KBController()

        self.actionsDict = {
            'button10': button10Actions(mouseController, keyboardController),
            'button11': button11Actions(mouseController, keyboardController),
            'button12': button12Actions(mouseController, keyboardController),
            'button13': button13Actions(mouseController, keyboardController),
            'button14': button14Actions(mouseController, keyboardController),
            'button15': button15Actions(mouseController, keyboardController),
        }

    def buttonPress(self, buttonName):
        if buttonName in self.buttons.keys():
            self.threadsHandler.runPressAction(self.actionsDict[buttonName].press)
            self.threadsHandler.runHoldAction(self.actionsDict[buttonName].hold, buttonName)

    def buttonRelease(self, buttonName):
        if buttonName in self.buttons.keys():
            self.threadsHandler.runReleaseAction(self.actionsDict[buttonName].release, buttonName)