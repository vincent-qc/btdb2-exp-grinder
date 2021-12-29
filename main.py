import pyautogui
import time
from util.position_parser import Parser
import util.map_finder

time.sleep(1)

print("Program Initiated")

game_counter = 0
map = None
finding_game = False #CHANGE BACK TO FALSE

p = Parser()

while True:
        # The variables and click function are seperated for readability
        
        battle_button_coords = pyautogui.locateOnScreen('data/images/buttons/battle-button.png', confidence = 0.6)
        hero_button_coords = pyautogui.locateOnScreen('data/images/buttons/hero-selection-button.png', confidence = 0.6)
        tower_button_coords = pyautogui.locateOnScreen('data/images/buttons/battle-button.png', confidence = 0.6)
        tower_screen_detect = pyautogui.locateOnScreen('data/images/buttons/tower-screen.png', confidence = 0.6)

        # Clicks the "Battle" button in the main menu
        if battle_button_coords != None and not finding_game:
            pyautogui.click(battle_button_coords)
            pyautogui.move(100, 100)
            finding_game = True
            print("Finding a game...")
            time.sleep(2)

        # Clicks the "Ready" button in hero selection
        elif hero_button_coords != None:
            pyautogui.click(hero_button_coords)
            print("Hero selected")
            time.sleep(2)

        # Clicks the "Battle" button in tower selection
        elif tower_screen_detect != None and finding_game:
            map = util.map_finder.get_map()

            pyautogui.click(tower_button_coords)
            finding_game = False
            print("Ready for game!")
            print("Playing on: " + map)
            time.sleep(6)

        back_button_coords = pyautogui.locateOnScreen('data/images/buttons/back-button.png', confidence = 0.6)
        if back_button_coords != None:
            pyautogui.click(back_button_coords)
            print("Discarding chest")
            time.sleep(2)

        ok_button_coords = pyautogui.locateOnScreen('data/images/buttons/ok-button.png', confidence = 0.8)
        if ok_button_coords != None:
            pyautogui.click(ok_button_coords)
            game_counter += 1
            print("Game Finished - Played a total of " + str(game_counter) + " games")
            time.sleep(2)

        is_right_side = None

        while pyautogui.locateOnScreen('data/images/ingame/surrender-button.png', confidence = 0.7) != None:

            if is_right_side == None:

                while pyautogui.locateOnScreen('data/images/ingame/locked-bloon.png', confidence = 0.7) == None:
                    time.sleep(1)

                is_right_side = pyautogui.locateCenterOnScreen('data/images/ingame/locked-bloon.png', confidence = 0.5)[0] > 960

                offset = 0 if is_right_side else 800
                tower_slot_x = 1790 if is_right_side else 130
                print("Playing on the " + ("right" if is_right_side else "left") + " side")
                time.sleep(1)

            
            for pos in p.get_positions(map, 'right' if is_right_side else 'left'):
                pyautogui.moveTo(tower_slot_x, 230)
                time.sleep(0.2)
                pyautogui.dragTo(pos[0], pos[1], 1.5, button='left')
                
            blue_bloon_coords = pyautogui.locateOnScreen('data/images/ingame/blue-bloon.png', confidence = 0.7)
            purple_bloon_coords = pyautogui.locateOnScreen('data/images/ingame/purple-bloons.png', confidence = 0.7)
            

            if purple_bloon_coords != None:

                print("Round 11 - Attempting to rush with purples")

                # Activate Bloon boost
                bloon_boost_coords = pyautogui.locateOnScreen('data/images/ingame/bloon-boost.png', confidence = 0.7)
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
