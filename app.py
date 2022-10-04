import pyautogui as gui
import time

def doIt():
    gui.click(button='right')
    print('FISH GET!')
    time.sleep(3)
    gui.click(button='right')

def autofish():
    while True:
        if gui.locateOnScreen('./images/toFindPtbrGui2.png', confidence=.9):
            doIt()
        elif gui.locateOnScreen('./images/toFindPtbrGui3.png', confidence=.9):
            doIt()
        elif gui.locateOnScreen('./images/toFindEnGui2.png', confidence=.9):
            doIt()
        elif gui.locateOnScreen('./images/toFindEnGui3.png', confidence=.9):
            doIt()

if __name__ == '__main__':
    print('STARTING...')
    time.sleep(5)
    print('FISHING!')
    gui.click(button='right')
    time.sleep(2)
    autofish()

# GAG DOES IT AGAIN
# MADE BY GAGUINHO CORP™®©