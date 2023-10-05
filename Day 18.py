i = 0
while(i<3):
    print(i)
    i += 1

x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break