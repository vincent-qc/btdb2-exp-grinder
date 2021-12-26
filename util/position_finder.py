import pyautogui
import keyboard
import time

while True:
    if keyboard.read_key() == "v":
        pos = pyautogui.position()
        
        print("\"" + str(round(pos[0] / 10) * 10) + " " + str(round(pos[1] / 10) * 10) + "\",")
        time.sleep(0.15)
# done: mayan, 
 