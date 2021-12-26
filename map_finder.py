import pyautogui

con_value = 0.5 # confidence value

def get_map():
    basalt = pyautogui.locateOnScreen('data/images/maps/basalt.png', confidence = con_value)
    if basalt != None:
        return "basalt"

    castle = pyautogui.locateOnScreen('data/images/maps/castle.png', confidence = con_value)
    if castle != None:
        return "castle"

    dino = pyautogui.locateOnScreen('data/images/maps/dino.png', confidence = con_value)
    if dino != None:
        return "dino"

    docks = pyautogui.locateOnScreen('data/images/maps/docks.png', confidence = con_value)
    if docks != None:
        return "docks"

    glade = pyautogui.locateOnScreen('data/images/maps/glade.png', confidence = con_value)
    if glade != None:
        return "glade"

    koru = pyautogui.locateOnScreen('data/images/maps/koru.png', confidence = con_value)
    if koru != None:
        return "koru"

    mayan = pyautogui.locateOnScreen('data/images/maps/mayan.png', confidence = con_value)
    if mayan != None:
        return "mayan"

    mines = pyautogui.locateOnScreen('data/images/maps/mines.png', confidence = con_value)
    if mines != None:
        return "mines"

    sands = pyautogui.locateOnScreen('data/images/maps/sands.png', confidence = con_value)
    if sands != None:
        return "sands"

    wall = pyautogui.locateOnScreen('data/images/maps/wall.png', confidence = con_value)

    if wall != None:
        return "wall"

    return "Error"
