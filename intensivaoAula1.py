import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1
time.sleep(2)

pyautogui.hotkey("ctrl", "t")
pyperclip.copy(
    "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(3)


pyautogui.click(x=438, y=277, clicks=2)

pyautogui.click(x=438, y=277, clicks=2)
