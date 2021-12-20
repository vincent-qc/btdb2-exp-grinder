from os import truncate
import pyautogui
import time
from PIL import Image

# To see X and Y coords and pixel color of your mouse enable the following line:
# pyautogui.mouseInfo()

time.sleep(1)

game_counter = 0 #counts the amount of games played
game_started = False #checks if the game has started
starting_xp = 0 #amount of xp gained each game

while True:

    if game_started == True:
        print("waiting for game...")
        in_game = pyautogui.pixel(x=956, y=63)

        if in_game == (121, 210, 38):

            is_on_the_right = pyautogui.pixel(x=133, y=162) # checks if playing on right or left side
            offset = 0 if is_on_the_right == (32, 135, 201) else 800 # Calculate offset
            tower_slot_x = 130 if offset == 0 else 1765 # calculates first tower slot

            if offset == 0: print("playing on LEFT side")
            else: print("playing on RIGHT side")

            time.sleep(3)

            for z in range (2): # placment system (this is temporary and will be changed soon to a better system)
                for x in range(250, 851, 100):
                    time.sleep(1)
                    pyautogui.moveTo(tower_slot_x, 230)
                    for y in range (400, 901, 100):
                        pyautogui.dragTo(x + offset, y, 0.4, button='left')
                time.sleep(12)

            time.sleep(3)

            game_started = False #restarts game loop for a new game

            while pyautogui.pixel(309, 153) != (255, 255, 255): # waits until it detects the defeated screen
                time.sleep(1)

            time.sleep(5)
            
            for i in range(120): # clicks on the ok button to return to main menu
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


    else: # get in a game
        
        time.sleep(3)
        pyautogui.click(x=1080, y=870) # click on battle button and ready button in the main menu and hero screen

        time.sleep(2)
        tower_button_color = pyautogui.pixel(x=612, y=708) # check if you are on the tower selection screen
        if tower_button_color == (57, 174, 228):
            pyautogui.click(x=1487, y=889)
            game_started = True # set game started to true
            time.sleep(1)

        pyautogui.click(317, 93) # click on back button(if you got new chests to discard)