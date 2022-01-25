"""
p037:控制电脑屏幕不锁屏


#鼠标手动移至4个角落时候，会FailSafeException
"""
import pyautogui
import random
import time

while True:
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    print(x, y)
    pyautogui.moveTo(x, y)
    time.sleep(2)