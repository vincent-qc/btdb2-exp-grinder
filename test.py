import pyautogui


menu_screenshot = pyautogui.screenshot(region=(1020, 10, 180, 32))
menu_screenshot.save('data/round-screenshot.jpeg')

pyautogui.click(x=1080, y=870)
pyautogui.mouseInfo()
