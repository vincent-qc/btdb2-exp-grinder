import pyautogui
import time
from PIL import Image
from PIL import ImageChops
import parser

time.sleep(1)

game_counter = 0
game_started = False
starting_xp = 0

#p = parser.Parser()

# TODO: the code is currently very buggy

while True:
    if game_started:
        #Take screenshots of the UI to see if the game is ready
        #print("Waiting for game...")

        # Check topmost pixel to see if game has started
        in_game = pyautogui.pixel(x=960, y=0)

        if in_game == (149, 85, 41):
            print("Game started!")

            # Check Sideline to see which side
            is_on_the_right = (pyautogui.pixel(x=200, y=40) == (163, 96, 50))

            print(is_on_the_right)

            # Calculate offset and tower positions
            offset = 0 if is_on_the_right else 800
            print(offset)

            tower_slot_x = 130 if is_on_the_right else 1790

            if is_on_the_right: print("playing on LEFT side")
            else: print("playing on RIGHT side")

            time.sleep(3)

            # for z in range (3):
            #
            #    # TODO: Get map name
            #    for pos in p.get_positions('MAP', 'right' if is_on_the_right else 'left'):
            #        pyautogui.moveTo(tower_slot_x, 230)
            #        pyautogui.dragTo(pos[0] + offset, pos[1], 1, button='left')
            #        time.sleep(0.3)
            #
            #    time.sleep(10)

            is_round_11 = False

            while pyautogui.pixel(x=1670, y=190) != (255, 255, 255):
                if is_round_11:
                    print("Round 11 - Attempting to rush with purples")
                    pyautogui.click(x = 35 if is_on_the_right else 1825, y=490)
                    time.sleep(0.4)

                    for _ in range(50):
                        pyautogui.click(x = 35 if is_on_the_right else 1825, y=490)
                        time.sleep(0.1)

                else:
                    round_screenshot = pyautogui.screenshot(region=(1020, 10, 180, 32))
                    round_reference = Image.open('data/round-reference.jpeg')

                    # Compare screenshots to see if it is round 11
                    is_round_11 = ImageChops.difference(round_screenshot, round_reference).getbbox() is None

                time.sleep(1)


            game_started = False
            pyautogui.click(x=1670, y=880)

            game_counter += 1

        else:
            pyautogui.click(304, 96)
            time.sleep(4)


    else: #get in a game
        
        # Clicks the "Battle" button in the main menu
        pyautogui.click(x=1080, y=870)
        time.sleep(2)

        # Clicks the "Ready" button in hero selection
        pyautogui.click(x=950, y=960)
        time.sleep(2)

        tower_button_color = pyautogui.pixel(x=1500, y=865)
        if tower_button_color == (255, 255, 255):
            pyautogui.click(x=1500, y=865)
            game_started = True
            time.sleep(1)

        time.sleep(1)

        # pyautogui.click(317, 93)

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
