import pyautogui as gui
import time

def autofish():
    while True:
        if gui.locateOnScreen('tofind.png', confidence=.7):
            gui.click(button='right')
            print('FISH GET!')
            time.sleep(3)
            gui.click(button='right')

if __name__ == '__main__':
    print('STARTING...')
    time.sleep(5)
    print('FISHING!')
    gui.click(button='right')
    time.sleep(2)
    autofish()

# GAG DOES IT AGAIN
# MADE BY GAGUINHO CORP™®©