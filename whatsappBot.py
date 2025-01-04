from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import keyboard as k
from urllib.parse import quote
import pyautogui
import time 

with open('message.txt', 'r') as file:
    msg = file.read()

msg = quote(msg)

numbers = []
with open('numbers.txt', 'r') as file:
    for num in file.readlines():
        numbers.append(num.rstrip())

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(15)

for num in numbers:

    link2 = f'https://web.whatsapp.com/send/?phone=91{num}&text={msg}'
    driver.get(link2)
    time.sleep(10)
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(1)  
    pyautogui.click(923,962)#attach button trigger
    time.sleep(1)
    pyautogui.click(999, 623)#photo/video if you want to send document than edit coordinate using coordinatefinder code
    time.sleep(2)
    pyautogui.click(131,438)#download button trigger
    time.sleep(1)
    pyautogui.click(463, 529)#edit here to choose your image or video or file using coordinatefinder code 
    time.sleep(2)
    pyautogui.click(707, 661)#open button trigger
    time.sleep(2)
    pyautogui.click(1855,927)#send button trigger
    time.sleep(5)

time.sleep(200)