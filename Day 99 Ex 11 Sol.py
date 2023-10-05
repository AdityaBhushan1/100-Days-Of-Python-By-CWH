from win32com.client import Dispatch

import os
import time 

REPEAT_INTERVAL = 5

s = Dispatch("SAPI.SpVoice")

while True:
    s.Speak(f"Hey Aditya Drink Water")
    time.sleep(REPEAT_INTERVAL)