#This project start with 3 coders: EichenbergerCHE, Bisdro, Awpii but if you like to contribute to us, add a motivational phrase in the "motivational.txt"

import subprocess
import random
import time

time.sleep(random.randint(900, 1800))
def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

file = open("motivational.txt", "r")
lineas = file.readlines()
number = random.randint(0, len(lineas)-1)
print(number)
sendmessage(str(lineas[number]))
file.close()
