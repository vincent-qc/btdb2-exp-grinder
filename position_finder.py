import pyautogui
import keyboard
import time

while True:
    if keyboard.read_key() == "v":
        print(pyautogui.position())
        time.sleep(0.15)
 