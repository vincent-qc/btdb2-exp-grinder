from cv2 import convertFp16
import pyautogui
import time
from PIL import Image
from PIL import ImageChops
from position_parser import Parser

time.sleep(3)

game_counter = 0

p = Parser()

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

        discard_chest_coords = pyautogui.locateOnScreen('data/images/discard-button.png', confidence = 0.6)
        if discard_chest_coords != None:
            pyautogui.click(discard_chest_coords)
            print("Discarding chest")
            time.sleep(2)

        ok_button_coords = pyautogui.locateOnScreen('data/images/ok-button.png', confidence = 0.8)
        if ok_button_coords != None:
            pyautogui.click(ok_button_coords)
            game_counter += 1
            print("Game Finished")
            time.sleep(2)

        is_right_side = None
        while pyautogui.locateOnScreen('data/images/surrender-button.png', confidence = 0.8) != None:

            if is_right_side == None:
                print(is_right_side)
                is_right_side = pyautogui.locateCenterOnScreen('data/images/locked-bloon.png', confidence = 0.8)[0] > 960
                print(is_right_side)
                offset = 0 if is_right_side else 800
                tower_slot_x = 130 if is_right_side else 1790
                print("Playing on the " + ("right" if is_right_side else "left") + " side")
                time.sleep(1)

            # TODO: add positions to maps.json
            #for pos in p.get_positions('MAP', 'right' if is_on_the_right else 'left'):
            #    pyautogui.moveTo(tower_slot_x, 230)
            #    pyautogui.dragTo(pos[0] + offset, pos[1], 1, button='left')
            #    time.sleep(0.3)

            purple_bloon_coords = pyautogui.locateOnScreen('data/images/purple-bloons.png', confidence = 0.8)
            blue_bloon_coords = pyautogui.locateOnScreen('data/images/blue-bloons.png', confidence = 0.8)
            
            if purple_bloon_coords != None:

                print("Round 11 - Attempting to rush with purples")

                # Activate Bloon boost
                bloon_boost_coords = pyautogui.locateOnScreen('data/images/bloon-boost.png', confidence = 0.8)
                pyautogui.click(bloon_boost_coords)
                time.sleep(0.4)

                # Click the purple bloons
                for _ in range(100):
                    pyautogui.click(purple_bloon_coords)
                    time.sleep(0.05)
            else:
                for _ in range(8):
                    pyautogui.click(blue_bloon_coords)
                    time.sleep(0.15)



            time.sleep(2)
