import time
import pyautogui  # pip install pyautogui

def spam(file):
    try:
        f = open(file, 'r').read()

    except Exception as e:
        return e

    else:
        time.sleep(7)  # tempo para abrir o app
        pyautogui.typewrite(f)
        pyautogui.press('ENTER')

        return 'Success'

print(spam(input('File: ')))