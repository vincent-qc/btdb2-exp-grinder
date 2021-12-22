import pyautogui

def get_map():
        basalt = pyautogui.locateOnScreen('data/images/maps/basalt.png', confidence = 0.8)
        if basalt != None:
            return "basalt"

        castle = pyautogui.locateOnScreen('data/images/maps/castle.png', confidence = 0.8)
        if castle != None:
            return "castle"

        dino = pyautogui.locateOnScreen('data/images/maps/dino.png', confidence = 0.8)
        if dino != None:
            return "dino"

        docks = pyautogui.locateOnScreen('data/images/maps/docks.png', confidence = 0.8)
        if docks != None:
            return "docks"

        glade = pyautogui.locateOnScreen('data/images/maps/glade.png', confidence = 0.8)
        if glade != None:
            return "glade"

        koru = pyautogui.locateOnScreen('data/images/maps/koru.png', confidence = 0.8)
        if koru != None:
            return "koru"

        mayan = pyautogui.locateOnScreen('data/images/maps/mayan.png', confidence = 0.8)
        if mayan != None:
            return "mayan"

        mines = pyautogui.locateOnScreen('data/images/maps/mines.png', confidence = 0.8)
        if mines != None:
            return "mines"

        sands = pyautogui.locateOnScreen('data/images/maps/sands.png', confidence = 0.8)
        if sands != None:
            return "sands"

        wall = pyautogui.locateOnScreen('data/images/maps/wall.png', confidence = 0.8)
        if wall != None:
            return "wall"

        return "Error"
