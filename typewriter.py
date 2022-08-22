import os
from tqdm import tqdm
import urllib.request
import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import pyautogui
from pynput.keyboard import Key, Controller



print("""

  _______                 ____        _   
 |__   __|               |  _ \      | |  
    | |_   _ _ __   ___  | |_) | ___ | |_ 
    | | | | | '_ \ / _ \ |  _ < / _ \| __|
    | | |_| | |_) |  __/ | |_) | (_) | |_ 
    |_|\__, | .__/ \___| |____/ \___/ \__|
        __/ | |                           
       |___/|_|     Author:     CuzImPixle
                    Version:    1
--------------------------------------------
""")
print("Login With Typewriter username and password:")
Username = input("Username:")
password = input("Password:")
tempo = input("Time between Letters (max 0.001s):")
for i in range(3):
    pbar = tqdm(["a", "b", "c", "d", "e"])
    for char in pbar:
        pbar.set_description("Loading:")
        time.sleep(0.125)

if urllib.request.urlopen(r"https://sg.typewriter.ch").getcode() == 200:
    print("Typewriter.sg is Online")
else:
    print("check internet connection and retry (This will close in 10s)")
    time.sleep(10)
    exit()
time.sleep(2)
os.system("cls")
print("""
--------------------------------------------

  _____ _   _ ______ ____  
 |_   _| \ | |  ____/ __ \ 
   | | |  \| | |__ | |  | |
   | | | . ` |  __|| |  | |
  _| |_| |\  | |   | |__| |
 |_____|_| \_|_|    \____/ 
                           
--------------------------------------------
""")
print("1.       Start a Lesson")
print("2.       Press esc to Start Bot")
print("3.       Enjoy")
print("NOTE:    ESC is for start and pause and for changing speed, if it doesnt pause hold down longer")


time.sleep(5)
ready = input("Are you ready? y/n  ")
if ready == "y":
    os.system("cls")

    pyautogui.PAUSE = float(tempo)
    specialcharakters = (u"ö", u"ü", u"ä")
    specialcharaktersBig = (u"Ö", u"Ü", u"Ä")


    def specialcharaktersS():
        if any(i in currentletter for i in specialcharakters):
            Controller().type(currentletter)


    def specialcharaktersB():
        if any(i in currentletter for i in specialcharaktersBig):
            Controller().press(Key.caps_lock)
            Controller().release(Key.caps_lock)
            time.sleep(float(tempo))
            Controller().type(currentletter)
            Controller().press(Key.caps_lock)
            Controller().release(Key.caps_lock)


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://sg.typewriter.ch/index.php?r=typewriter/runLevel")
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="LoginForm_username"]').send_keys(Username)
    driver.find_element(By.XPATH, '//*[@id="LoginForm_pw"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()
    while True:
        if keyboard.is_pressed("esc"):
            try:
                driver.find_element(By.XPATH, '//*[@id="actualLetter"]')
                time.sleep(0.1)
                currentletter = driver.find_element(By.XPATH, '//*[@id="actualLetter"]').text
                specialcharaktersB()
                specialcharaktersS()
                pyautogui.typewrite(currentletter)
                rem = driver.find_element(By.XPATH, '//*[@id="amountRemaining"]').text
                # print(type(rem))
                for i in range(int(rem)):
                    rem = driver.find_element(By.XPATH, '//*[@id="amountRemaining"]').text
                    currentletter = driver.find_element(By.XPATH, '//*[@id="actualLetter"]').text
                    specialcharaktersB()
                    specialcharaktersS()
                    pyautogui.typewrite(currentletter)
                    if keyboard.is_pressed("esc"):
                        time.sleep(1)
                        tempo = input("Time between Letters (max 0.001s):")
                        pyautogui.PAUSE = float(tempo)
                        break

            except NoSuchElementException:
                time.sleep(0.1)