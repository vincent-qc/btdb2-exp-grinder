import pyautogui
import time
from PIL import Image
from PIL import ImageChops

eco_screenshot = pyautogui.screenshot(region=(1800, 200, 100, 100))
eco_screenshot.save('nametag.jpeg')
