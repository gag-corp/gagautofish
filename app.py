import pyautogui as gui
import time

def doIt():
    gui.click(button='right')
    time.sleep(2.45)
    gui.click(button='right')

def resetFishingRod():
    print('FISHING ROD IS NOT IN THE WATER, RESTARTING...')
    gui.scroll(1000)
    time.sleep(0.5)
    gui.scroll(-1000)
    time.sleep(0.5)
    gui.click(button='right')
    autofish()

def autofish():
    while gui.locateOnScreen('./images/respingos.png', grayscale=True, confidence=0.4):
        if gui.locateOnScreen('./images/toFindPtbrGui2.png', confidence=.9):
            doIt()
            print('FISH CAUGHT')
        elif gui.locateOnScreen('./images/toFindPtbrGui3.png', confidence=.9):
            doIt()
            print('FISH CAUGHT')
        elif gui.locateOnScreen('./images/toFindEnGui2.png', confidence=.9):
            doIt()
            print('FISH CAUGHT')
        elif gui.locateOnScreen('./images/toFindEnGui3.png', confidence=.9):
            doIt()
            print('FISH CAUGHT')
    resetFishingRod()
    
if __name__ == '__main__':
    print('STARTING...')
    time.sleep(5)
    print('FISHING!')
    gui.click(button='right')
    time.sleep(2)
    autofish()

# GAG DOES IT AGAIN
# MADE BY GAGUINHO CORP™®©