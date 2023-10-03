import pyautogui as p
from time import sleep

n = int(input())
sleep(5)

for i in range(1,n+1):
    p.write("#" * i, interval= 0.1)
    p.write("\n", interval= 0.1)
