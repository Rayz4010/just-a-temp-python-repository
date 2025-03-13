'''
Psudocode:
importing the pyautogui module
importing the time module
and  using pyautogui to automate message
'''

#importing modules
import pyautogui
import time 

#the timer to act 
time.sleep(4)

#a open loop to become a menance 
count=0
while count<=1000:
    #automation
    pyautogui.typewrite("thats not cool man") 
    pyautogui.press("enter")
    count=count+1 


'''
This is the  end of the code
'''
