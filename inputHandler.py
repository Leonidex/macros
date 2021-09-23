"""
Input handling class, listens to the mouse (and keyboard if implemented) and send the acquired data to the macros handler.
"""

# from pynput.keyboard import Listener  as KeyboardListener
from pynput.mouse import Listener as MouseListener
# from pynput.keyboard import Key

class inputHandler:
    def __init__(self, macrosHandler):
        self.macrosHandler = macrosHandler

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.macrosHandler.buttonPress(button.name)
        else:
            self.macrosHandler.buttonRelease(button.name)

    def start(self):
        with MouseListener(on_click=self.on_click) as listener:
            # with KeyboardListener(on_press=on_press) as listener:
                listener.join()