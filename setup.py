import pyautogui
import time
from PIL import Image
from PIL import ImageChops


#####################################################################
############################ DISCLAIMER #############################
############# COMMENT OUT VARIABLES AND RUN THIS SCRIPT #############
################### OVER AND OVER TO WHEN REQUIRED ##################
#####################################################################

# Change coords to make it screenshot the 'ready' button (x, y, width, height)
menu_screenshot = pyautogui.screenshot(region=(960, 810, 240, 120))
menu_screenshot.save('menu.jpeg')

# Change coords to make it screenshot the 'ready' button during hero selection (x, y, width, height)
hero_screenshot = pyautogui.screenshot(region=(830, 900, 260, 120))
hero_screenshot.save('hero-selection.jpeg')

# Change coords to make it screenshot the 'ready' button during tower selection (x, y, width, height)
hero_screenshot = pyautogui.screenshot(region=(1400, 830, 200, 110))
hero_screenshot.save('tower-selection.jpeg')

# Change coords to make it screenshot the 'ready' button during tower selection (x, y, width, height)
hero_screenshot = pyautogui.screenshot(region=(1400, 830, 200, 110))
hero_screenshot.save('tower-selection.jpeg')

# Change it to screenshot the starting 'eco' at the top of the screen
eco_screenshot = pyautogui.screenshot(region=(900, 0, 120, 40))
eco_screenshot.save('eco.jpeg')

# Change it to screenshot the right of the screen (only when you are playing on the left side)
# ignore the 'nametag' variable name, i forgor to change
nametag_screenshot = pyautogui.screenshot(region=(1800, 200, 100, 100))
nametag_screenshot.save('nametag-screenshot.jpeg')