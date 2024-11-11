import pyautogui
import time

def click():
    pass
def check_screen():
    time.sleep(5)
    print(pyautogui.locateOnScreen('image2.png', confidence=0.7))

def main():
    check_screen()

if __name__ == "__main__":
    main()