#import all the necessaries
from multiprocessing.connection import wait
import pyautogui
import time
import random

#load file 'preferences' and if not exist create it with values: 'lang: en', 'search: firefox', 'webBrowserIconNum: 0'
try:
    with open('preferences', 'r') as f:
        #get the value from all the lines in the file
        lang = f.readline().split(':')[1].strip()
        search = f.readline().split(':')[1].strip()
        webBrowserIconNum = int(f.readline().split(':')[1].strip())
except FileNotFoundError:
    with open('preferences', 'w') as f:
        f.write('lang: en\n')
        f.write('search: firefox\n')
        f.write('webBrowserIconNum: 0\n')
        print("preferences file created, the program will close in 5 seconds")
        time.sleep(5)
    exit()

print(lang)
print(search)
print(webBrowserIconNum)

#download github file at the url: 

# #click on the pixel: 317, 750 using pyautogui
# pyautogui.click(317, 750)

# #then do a variable to store the location of the pixel: 300, 65
# FireSearchBar = pyautogui.pixel(300, 65)

# #wait 1.5s
# time.sleep(1.5)

# #click on it
# pyautogui.click(300, 65)

# #enter the word "google" and press enter
# pyautogui.typewrite("bing", interval=0.1)
# pyautogui.press("enter")

# #get the 20, 20 pixel color and if its rgba(16,110,191,255) then set the mouse to the pixel: 450, 250 and if not print the color with rgba and ait 0.5s and repeat
# matches = False
# while matches == False:
#     if pyautogui.pixelMatchesColor(20, 20, (16, 110, 191, 255)):
#         pyautogui.moveTo(450, 250)
#         matches = True
#     else:
#         matches = False
#         time.sleep(0.5)

# #enter random word with a-z A-Z 0-9 and with 10 characters
# random_word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
# pyautogui.typewrite(random_word, interval=0.05)
# pyautogui.press("enter")

# #do a loop that repeat 20 times so the cursor move first to the pixel 400, 150 then press backspace 10 times then redo the same thing of the random word but wait 1s after each times
# for i in range(1):
#     pyautogui.click(400, 150)
#     for i in range(10):
#         pyautogui.press("backspace")
#     random_word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
#     pyautogui.typewrite(random_word, interval=0.01)
#     pyautogui.press("enter")
#     time.sleep(0.75)