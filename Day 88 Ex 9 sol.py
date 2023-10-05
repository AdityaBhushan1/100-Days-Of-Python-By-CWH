from win32com.client import Dispatch

s = Dispatch("SAPI.SpVoice")

l = ["Rahul", "Nishant", "Harry"]
for i in l:
    s.Speak(f"Shoutout to {i}")