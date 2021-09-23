"""
Main file for running the macros program.
"""
import logging
import macrosHandler
import inputHandler

if __name__ == "__main__":
    logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
    # _thread = threading.Thread(target=initMacrosHandler, args=(), daemon=True)
    _macrosHandler = macrosHandler.macrosHandler()
    _inputHandler = inputHandler.inputHandler(_macrosHandler)
    _inputHandler.start()