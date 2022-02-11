
from selenium import webdriver
import pyautogui
import time
import os

#this data for login to outlook0
password = "Ha@2000780"
email = "hassan20-00780@student.eelu.edu.eg"

#outlook url
url = "https://outlook.office365.com/mail/"

#step1
#this for open the browser and emile website 
driver = webdriver.Chrome("C:\ChromeDriver\chromedriver.exe")
driver.maximize_window()
driver.get(url)

#step2
#wirte email and press next
time.sleep(3)
driver.find_element_by_id("i0116").send_keys(email)
driver.find_element_by_id("idSIButton9").click()

#step3
#write password and press next
time.sleep(2)
driver.find_element_by_id("i0118").send_keys(password)
time.sleep(2)
driver.find_element_by_id("idSIButton9").click()
driver.find_element_by_id("idSIButton9").click()

#step4
#here we need to define constractor id to get the meeting link
nohaId = "AQAAACyy7qwBAAABNTX8NAAAAAA="
time.sleep(3)
driver.find_element_by_id(nohaId).click()


#step5
#define join meeting id to click it to get link
time.sleep(10)
driver.find_element_by_partial_link_text("Join meeting").click()

#step6 open meeting applection on desktop and join meeting
time.sleep(10)
pyautogui.click(1054,210)
time.sleep(5)
pyautogui.click(1096,1015)

#step7 
#open the recorder and record the section
time.sleep(10)
os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\Programs\\OBS Studio\\OBS Studio (64bit).lnk")

time.sleep(5)
#start recording
pyautogui.press('enter')

#mimize the screen
time.sleep(5)
pyautogui.hotkey('win', '4')

#maxmiz the screen
time.sleep(5)
pyautogui.hotkey('win', '4')

#stop recording
time.sleep(5)
pyautogui.press('enter')

#close the recorder
time.sleep(2)
pyautogui.hotkey('alt', 'f4')
time.sleep(3)
#clase the meeting app
pyautogui.click(1047,1079)
time.sleep(3)
pyautogui.click(865,492)