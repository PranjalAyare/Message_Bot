import pyautogui as auto
import time
time.sleep(10)
N = 100
while True:
    N -= 1
    auto.write(int())
    auto.press('enter')
    if N== 0:
      break


