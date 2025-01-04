import pyautogui as pg
import time

while True:
    time.sleep(8)
    x,y=pg.position()
    print(x,y)
