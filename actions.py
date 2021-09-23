"""
This file contains the actual macros that are to be performed with every press, hold and release of each button.
"""

from pynput.mouse import Button as MouseButton
from pynput.keyboard import Key as Key
import time

class buttonActions:
    def __init__(self, mouseController, kBController):
        self.mouseController = mouseController
        self.kBController = kBController

class button10Actions(buttonActions): # Up button left of left click
    def __init__(self, mouseController, kBController):
        super().__init__(mouseController, kBController)

    def press(self):
        pass
    
    def hold(self):
        pass

    def release(self):
        pass

class button11Actions(buttonActions): # Down button left of left click
    def __init__(self, mouseController, kBController):
        super().__init__(mouseController, kBController)

    def press(self):
        pass
    
    def hold(self):
        pass

    def release(self):
        pass

class button12Actions(buttonActions): # Main thumb button
    def __init__(self, mouseController, kBController):
        super().__init__(mouseController, kBController)

    def press(self):
        pass
    
    def hold(self):
        pass

    def release(self):
        pass

class button13Actions(buttonActions): # Up thumb button
    def __init__(self, mouseController, kBController):
        super().__init__(mouseController, kBController)

    def press(self):
        pass
    
    def hold(self):
        self.mouseController.press(MouseButton.left)
        time.sleep(0.01)
        self.mouseController.release(MouseButton.left)

    def release(self):
        self.mouseController.release(MouseButton.left)

class button14Actions(buttonActions): # Down thumb button
    def __init__(self, mouseController, kBController):
        super().__init__(mouseController, kBController)

    def press(self):
        pass
    
    def hold(self):
        self.mouseController.press(MouseButton.right)
        time.sleep(0.01)
        self.mouseController.release(MouseButton.right)

    def release(self):
        self.mouseController.release(MouseButton.right)

class button15Actions(buttonActions): # Little middle button
    def __init__(self, mouseController, kBController):
        super().__init__(mouseController, kBController)

    def press(self):
        pass
    
    def hold(self):
        pass

    def release(self):
        pass
