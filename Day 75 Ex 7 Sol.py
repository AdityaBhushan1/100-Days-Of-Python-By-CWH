import os

files = os.listdir("Day 75 Ex 7 Sol")
i = 1
for file in files:
    if file.endswith(".png"):
        os.rename(f"Day 75 Ex 7 Sol/{file}",f"Day 75 Ex 7 Sol/{i}.png")
        i += 1