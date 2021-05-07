#this is a simple spam bot all u have to is to put cursor to the palce u want want to spam after running the 
#code in ur pc.
#made by Ajay aka alex4202000


from pynput.keyboard import Key, Controller
import time
message="don't spam" #here u can write anything u want
keyboard=Controller()
time.sleep(10) #after 10 seconds the spam will start

for num in range(500): #this is the number of times the msg will be delivered
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)    
    keyboard.release(Key.enter)  
    time.sleep(.1) #this is the interval time between two msgs
