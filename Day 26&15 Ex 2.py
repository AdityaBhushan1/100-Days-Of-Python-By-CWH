import time
timestamp = int(time.strftime('%H'))
# timestamp = 
# print(timestamp)
name = input("Entre Your Name: ")
if timestamp >= 4 and  timestamp < 12:
    print(f"Good Morning, {name}!")
elif timestamp >= 12 and timestamp < 16:
    print(f"Good After Noon {name}!")
elif timestamp >= 16 and timestamp < 21:
    print(f"Good Evening {name}!")
else:
    print(f"Good Night {name}!") 




# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# # https://docs.python.org/3/library/time.html#time.strftime