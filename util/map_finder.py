import pyautogui

con_value = 0.4  # confidence value


def get_map():
    basalt = pyautogui.locateOnScreen(
        'data/images/maps/basalt.png',
        confidence=con_value)
    if basalt is not None:
        return "basalt"

    castle = pyautogui.locateOnScreen(
        'data/images/maps/castle.png',
        confidence=con_value)
    if castle is not None:
        return "castle"

    dino = pyautogui.locateOnScreen(
        'data/images/maps/dino.png',
        confidence=con_value)
    if dino is not None:
        return "dino"

    docks = pyautogui.locateOnScreen(
        'data/images/maps/docks.png',
        confidence=con_value)
    if docks is not None:
        return "docks"

    glade = pyautogui.locateOnScreen(
        'data/images/maps/glade.png',
        confidence=con_value)
    if glade is not None:
        return "glade"

    koru = pyautogui.locateOnScreen(
        'data/images/maps/koru.png',
        confidence=con_value)
    if koru is not None:
        return "koru"

    mayan = pyautogui.locateOnScreen(
        'data/images/maps/mayan.png',
        confidence=con_value)
    if mayan is not None:
        return "mayan"

    mines = pyautogui.locateOnScreen(
        'data/images/maps/mines.png',
        confidence=con_value)
    if mines is not None:
        return "mines"

    sands = pyautogui.locateOnScreen(
        'data/images/maps/sands.png',
        confidence=con_value)
    if sands is not None:
        return "sands"

    wall = pyautogui.locateOnScreen(
        'data/images/maps/wall.png',
        confidence=con_value)

    if wall is not None:
        return "wall"

    print("\n NOTICE: An error has occured while determining the map. \nYou will need to restart the bot and to try again\n")
    return "Error"
