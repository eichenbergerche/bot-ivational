#This project start with 3 coders: EichenbergerCHE, Bisdro, Awpii but if you like to contribute to us, add a motivational phrase in the "motivational.txt"

import subprocess
import random
import time
import platform
from win10toast import ToastNotifier

time.sleep(random.randint(900, 1800))
def sendmessage(message): #add suport to windows
    if(platform.system=="linux"): 
        subprocess.Popen(['notify-send', message])
        return
    else:
        toaster = ToastNotifier()
        toaster.show_toast("",message)


file = open("motivational.txt", "r")
lineas = file.readlines()
number = random.randint(0, len(lineas)-1)
print(number)
sendmessage(str(lineas[number]))
file.close()