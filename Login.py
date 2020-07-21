# Code to check if right mouse buttons were pressed
import win32api
import time
import pyautogui as pag
state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
email = "Your_Email_Here!"
password = "Your_Password_Here!"
while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)
    if a != state_left:  # Button state changed
        state_left = a
        print(a)
        if a < 0:
            pag.typewrite(email)
            time.sleep(0.1)
            pag.press('tab')
            time.sleep(0.1)
            pag.typewrite(password)
            pag.press('enter')
