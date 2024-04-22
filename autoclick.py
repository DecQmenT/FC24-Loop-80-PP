import time 
import threading
from pynput.mouse import Controller
from pynput.keyboard import Listener, KeyCode
import pyautogui

TOGGLE_KEY = KeyCode(char="q")

clicking = False
mouse = Controller()

def clicker():
    global clicking
    while True:
        if clicking:
            pyautogui.leftClick(1300, 500)
            time.sleep(2)
            pyautogui.leftClick(1750, 900)
            time.sleep(0.01)
            pyautogui.leftClick(1741, 617)
            time.sleep(0.01)
            pyautogui.leftClick(1707, 809)
            time.sleep(0.01)
            pyautogui.scroll(-200)
            time.sleep(0.01)
            pyautogui.leftClick(1800, 1000)
            clicking = not clicking
        time.sleep(0.1)

def toggle_event(key):
    global clicking
    if key == TOGGLE_KEY:
        clicking = not clicking
        print(clicking)

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
