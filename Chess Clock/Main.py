# Created by Sayo
# If u have any problems using it or found any bugs msg me on discord: Sayo ツ#9954



from asyncio import sleep
from turtle import Terminator
import pyautogui
import pydirectinput 
import keyboard  
import time
import pynput
import math
import os

def clear_console():
    os.system('cls')

Pass = True
MainPass = True
PassTime1 = True


while (Pass):
    MainTime = int(input("How long do u want the time to be? (in min):"))
    if (MainTime == "") :
        print("Wrong input!")
    else:
        Pass = False


MainTimeS = MainTime * 60
TimeP1 = int(MainTimeS)
TimeP2 = int(MainTimeS)

TimeP1Min = round(TimeP1 / 60)
TimeP1Sec = 0

TimeP2Min = round(TimeP1 / 60)
TimeP2Sec = 0



while (MainPass):

    while(PassTime1 == True):   
        for i in range(10):
            if keyboard.is_pressed("space"):
                
                PassTime1 = False
            time.sleep(0.1)



        if TimeP1Sec == 0:
            TimeP1Min = TimeP1Min - 1
            TimeP1Sec = 60

        if TimeP1Min == -1:
            MainPass = False
            break

        TimeP1Sec = TimeP1Sec - 1

        clear_console()
        print (f"{round(TimeP1Min)}:{TimeP1Sec}  |  {round(TimeP2Min)}:{TimeP2Sec}")

    while(PassTime1 == False):
        for i in range(10):
            if keyboard.is_pressed("space"):
                PassTime1 = True
                
            time.sleep(0.1)



        if TimeP2Sec == 0:
            TimeP2Min = TimeP2Min - 1
            TimeP2Sec = 60

        if TimeP2Min == -1:
            MainPass = False
            break

        TimeP2Sec = TimeP2Sec - 1

        clear_console()
        print (f"{round(TimeP1Min)}:{TimeP1Sec}  |  {round(TimeP2Min)}:{TimeP2Sec}")

