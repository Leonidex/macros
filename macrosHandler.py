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
        # self.buttonName = ''
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

    # def run(self):
    #     # print(self.buttonName)
    #     # TODO: Replace with match-case once python 3.10 comes out
    #     if self.buttonName == 'button10': # Up button left of left click
    #         pass
    #     elif self.buttonName == 'button11': # Down button left of left click
    #         pass
    #     elif self.buttonName == 'button12': # Main thumb button
    #         pass
    #         if self.buttons[self.buttonName] is True:
    #             self.keyboardController.press(Key.f1)
    #         else:
    #             self.keyboardController.release(Key.f1)
    #     elif self.buttonName == 'button13': # Up thumb button
    #         if self.buttons[self.buttonName] is True:
    #             self.mouseController.press(MouseButton.left)
    #             time.sleep(0.002)
    #             self.mouseController.release(MouseButton.left)
    #         else:
    #             self.mouseController.release(MouseButton.left)
    #             self.buttonName = None
    #     elif self.buttonName == 'button14': # Down thumb button
    #         if self.buttons[self.buttonName] is True:
    #             self.mouseController.press(MouseButton.right)
    #             time.sleep(0.001)
    #             self.mouseController.release(MouseButton.right)
    #         else:
    #             self.mouseController.release(MouseButton.right)
    #             self.buttonName = None
    #     elif self.buttonName == 'button15': # Little middle button
    #         pass

    # def buttonPress(self, buttonName):
    #     # print('pressed_{0}'.format(buttonName))
    #     # print(buttonName in self.buttons.keys())
    #     if buttonName in self.buttons.keys():
    #         self.buttonName = buttonName
    #         self.buttons[buttonName] = True

    # def buttonRelease(self, buttonName):
    #     # print('released {0}'.format(buttonName))
    #     if buttonName in self.buttons.keys():
    #         self.buttonName = buttonName
    #         self.buttons[buttonName] = False

    def buttonPress(self, buttonName):
        # print('pressed_{0}'.format(buttonName))
        # print(buttonName in self.buttons.keys())
        if buttonName in self.buttons.keys():
            self.threadsHandler.runPressAction(self.actionsDict[buttonName].press)
            self.threadsHandler.runHoldAction(self.actionsDict[buttonName].hold, buttonName)

    def buttonRelease(self, buttonName):
        # print('released {0}'.format(buttonName))
        if buttonName in self.buttons.keys():
            self.threadsHandler.runReleaseAction(self.actionsDict[buttonName].release, buttonName)