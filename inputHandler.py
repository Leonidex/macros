"""
Input handling class, listens to the mouse (and keyboard if implemented) and send the acquired data to the macros handler.
"""

# from pynput.keyboard import Listener  as KeyboardListener
from pynput.mouse import Listener as MouseListener
# from pynput.keyboard import Key

class inputHandler:
    def __init__(self, macrosHandler):
        self.macrosHandler = macrosHandler

    # def end_rec(key):
    #     print(str(key))

    # def on_press(key):
    #     print(str(key))

    # def on_move(x, y):
    #     print("Mouse moved to ({0}, {1})".format(x, y))

    def on_click(self, x, y, button, pressed):
        if pressed:
            # print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
            self.macrosHandler.buttonPress(button.name)
            # pyautogui.moveRel(0, 10)
        else:
            # print('released')
            self.macrosHandler.buttonRelease(button.name)

    # def on_scroll(x, y, dx, dy):
    #     print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    def start(self):
        with MouseListener(on_click=self.on_click) as listener:
            # with KeyboardListener(on_press=on_press) as listener:
                listener.join()