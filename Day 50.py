# with open("Day 50.txt",'r') as f:
#     while True:
#         line = f.readline()
#         print(line)
#         if not line:
#             break

with open("Day 50.txt",'a') as f:
    lines = ['\nline 1\n','line2\n','line3\n']
    f.writelines(lines)