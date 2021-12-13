import pyautogui
import time
from PIL import Image
from PIL import ImageChops

time.sleep(1)

game_started = False
exp_earned = 0

battlebutton = Image.open("battle-button.jpeg")
herobutton = Image.open("hero-selection.jpeg")
towerbutton = Image.open("tower-selection.jpeg")
ecoimage = Image.open("eco.jpeg")
sidelineimage = Image.open("sideline.jpeg")

while True:

    if game_started:

        # Take screenshots of the UI to see if the game is ready
        eco_screenshot = pyautogui.screenshot(region=(900, 0, 120, 40))
        eco_screenshot.save('eco-screenshot.jpeg')
        eco_ready = ImageChops.difference(Image.open("eco-screenshot.jpeg"), ecoimage)

        if eco_ready.getbbox() is None:

            # Check Sideline to see which side
            sideline_screenshot = pyautogui.screenshot(region=(1800, 200, 100, 100))
            sideline_screenshot.save('sideline-screenshot.jpeg')
            sideline_screenshot = Image.open("sideline-screenshot.jpeg")
            compare_sideline = ImageChops.difference(sideline_screenshot, sidelineimage)

            # Calculate offset and tower positions
            offset = 0 if compare_sideline.getbbox() is None else 960
            tower_slot_x = 80 if offset == 0 else 1840

            print(compare_sideline.getbbox())

            print("Eco Ready \nOffset: " + str(offset))
            time.sleep(3)

            for x in range(200, 800, 80):
                pyautogui.moveTo(tower_slot_x, 230)
                for y in range (100, 700, 200):
                    pyautogui.dragTo(x + offset, y, 0.14, button='left')

            game_started = False

            pyautogui.click(960, 1040)
            time.sleep(1)
            pyautogui.click(1480 if offset == 960 else 650, 640)

            time.sleep(5)

            for x in range(50):
                pyautogui.click(1640, 900)
                time.sleep(0.1)

            exp_earned += 300

            print("----------------------")
            print("Exp Earned: " + str(exp_earned) + "\n")
            print("----------------------\n")

        else:
            pyautogui.click(300, 300)
            time.sleep(4)

            
    else:
        menu_screenshot = pyautogui.screenshot(region=(960, 810, 240, 120))
        menu_screenshot.save('menu-screenshot.jpeg')

        hero_screenshot = pyautogui.screenshot(region=(830, 900, 260, 120))
        hero_screenshot.save('hero-screenshot.jpeg')

        tower_screenshot = pyautogui.screenshot(region=(1400, 830, 200, 110))
        tower_screenshot.save('tower-screenshot.jpeg')
        

        on_menu = ImageChops.difference(Image.open("menu-screenshot.jpeg"), battlebutton)
        on_hero_selection = ImageChops.difference(Image.open("hero-screenshot.jpeg"), herobutton)
        on_tower_selection = ImageChops.difference(Image.open("tower-screenshot.jpeg"), towerbutton)

        if on_menu.getbbox() is None:
            pyautogui.click(x=960, y=810)
            print("Seraching for Game...")
            time.sleep(4)

        elif on_hero_selection.getbbox() is None:
            pyautogui.click(x=830, y=900)
            print("Selected Hero")

            time.sleep(1)

        elif on_tower_selection.getbbox() is None:
            pyautogui.click(x=1400, y=830)
            game_started = True
            print("Ready For Game")
        
        else:
            pyautogui.click(1640, 900)
            time.sleep(0.3)
            pyautogui.click(x=1400, y=700)
            time.sleep(0.3)
            pyautogui.click(x=100, y=460)

        time.sleep(3)


screenshot_initial = pyautogui.screenshot(region=(960, 810, 240, 120))
screenshot_initial.save('screenshotinit.jpeg')


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
