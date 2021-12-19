from os import truncate
import pyautogui
import time
from PIL import Image


time.sleep(1)

game_counter = 0
game_started = False
starting_xp = 0

while True:

    if game_started == True:
        #Take screenshots of the UI to see if the game is ready
        print("waiting for game...")
        in_game = pyautogui.pixel(x=956, y=63)
        if in_game == (121, 210, 38):
            print("game started!")
            # Check Sideline to see which side
            is_on_the_right = pyautogui.pixel(x=133, y=162)

            # Calculate offset and tower positions
            offset = 0 if is_on_the_right == (32, 135, 201) else 800
            print(offset)
            tower_slot_x = 130 if offset == 0 else 1765

            if offset == 0: print("playing on LEFT side")
            else: print("playing on RIGHT side")

            time.sleep(3)

            for z in range (2):
                for x in range(250, 851, 100):
                    time.sleep(1)
                    pyautogui.moveTo(tower_slot_x, 230)
                    for y in range (400, 901, 100):
                        pyautogui.dragTo(x + offset, y, 0.4, button='left')
                time.sleep(12)

            time.sleep(3)

            # for x in range(3):
            #     time.sleep(10)
            #     keyboard.press_and_release('SPACE')

            game_started = False
            #918,611
            while pyautogui.pixel(309, 153) != (255, 255, 255):
                time.sleep(1)
            
            # pyautogui.click(952, 1000) surrender
            # time.sleep(1)
            # pyautogui.click(1432 if offset == 960 else 700, 640)
            time.sleep(5)
            
            for i in range(120):
                pyautogui.click(x=1670, y=880)
                time.sleep(0.1)

            game_counter += 1
            starting_xp += 330
            print("----------------------")
            print("Game number " + str(game_counter) + " is  done!")
            print("your tower xp is: " + str(starting_xp))
            print("----------------------")

        else:
            pyautogui.click(304, 96)
            time.sleep(4)


    else: #get in a game
        
        time.sleep(3)
        pyautogui.click(x=1080, y=870)

        time.sleep(2)
        tower_button_color = pyautogui.pixel(x=612, y=708)
        if tower_button_color == (57, 174, 228):
            pyautogui.click(x=1487, y=889)
            game_started = True
            time.sleep(1)

        pyautogui.click(317, 93)

        # menu_button_color = pyautogui.pixel(x=936, y=874)
        # menu_button_color2 = pyautogui.pixel(x=969, y=879)
        # if menu_button_color == (255, 201, 0) and menu_button_color2 == (0, 0, 0):
        #     pyautogui.click(x=1080, y=870)
        #     print("Seraching for Game...")
        #     time.sleep(1)

        # hero_button_color = pyautogui.pixel(x=949, y=432)
        # if hero_button_color == (3, 176, 254):
        #     pyautogui.click(x=951, y=977)
        #     print("Selected Hero")
        #     time.sleep(1)

        # tower_button_color = pyautogui.pixel(x=926, y=81)
        # if tower_button_color == (172, 0, 0):
        #     pyautogui.click(x=1487, y=889)
        #     game_started = True
        #     print("Ready For Game")
        #     time.sleep(1)
        


# Hero Ready
# region=(830, 900, 260, 120)

# Tower Ready
# (1400, 830, 200, 110)

# Name Tag
# (1800, 200, 100, 100)

# Ok Button
# (1630, 864, 80, 80)

# Tower Slot
# (x=80, y=230) or (x=1900, y=230)

# Window Bounds
# (x=200, y=200) to (x=880, y=960)
