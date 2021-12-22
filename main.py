from cv2 import convertFp16
import pyautogui
import time
from PIL import Image
from PIL import ImageChops
import parser

time.sleep(3)

game_counter = 0
game_started = False
starting_xp = 0

#p = parser.Parser()

# TODO: the code is currently very buggy

while True:
        # The variables and click function are seperated for readability
        
        # Clicks the "Battle" button in the main menu
        battle_button_coords = pyautogui.locateOnScreen('data/images/battle-button.png', confidence = 0.6)

        if battle_button_coords != None:
            pyautogui.click(battle_button_coords)
            pyautogui.move(100, 100)
            print("Finding a game...")
            time.sleep(2)

        # Clicks the "Ready" button in hero selection
        hero_button_coords = pyautogui.locateOnScreen('data/images/hero-selection-button.png', confidence = 0.6)
        if hero_button_coords != None:
            pyautogui.click(hero_button_coords)
            print("Hero selected")
            time.sleep(2)

        # Clicks the "Battle" button in tower selection
        tower_button_coords = pyautogui.locateOnScreen('data/images/tower-selection-button.png', confidence = 0.6)
        if tower_button_coords != None:
            pyautogui.click(tower_button_coords)
            print("Ready for game!")
            time.sleep(2)


        is_right_side = None
        while pyautogui.pixelMatchesColor(960, 200, (147, 80, 28)):

            if is_right_side == None:
                is_right_side = pyautogui.pixelMatchesColor(1830, 220, (134, 70, 26))
                offset = 0 if is_right_side else 800
                tower_slot_x = 130 if is_right_side else 1790
                print("Playing on the " + ("right" if is_right_side else "left") + " side")
                time.sleep(1)

            #for pos in p.get_positions('MAP', 'right' if is_on_the_right else 'left'):
            #    pyautogui.moveTo(tower_slot_x, 230)
            #    pyautogui.dragTo(pos[0] + offset, pos[1], 1, button='left')
            #    time.sleep(0.3)
            purple_bloon_coords = pyautogui.locateOnScreen('data/images/purple-bloons.png', confidence = 0.6)
            blue_bloon_coords = pyautogui.locateOnScreen('data/images/blue-bloons.png', confidence = 0.6)
            
            if purple_bloon_coords != None:

                print("Round 11 - Attempting to rush with purples")

                # Activate Bloon boost
                bloon_boost_coords = pyautogui.locateOnScreen('data/images/bloon-boost.png')
                pyautogui.click(bloon_boost_coords)
                time.sleep(0.4)

                # Click the purple bloons
                for _ in range(50):
                    pyautogui.click(purple_bloon_coords)
                    time.sleep(0.15)
            else:
                for _ in range(8):
                    pyautogui.click(blue_bloon_coords)
                    time.sleep(0.15)


            time.sleep(1)
