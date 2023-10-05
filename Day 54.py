a = 4
b = "4"

print(a is b) # compares the exact location of object in memmory
print(a==b) # compares the value

a = [1,2,43]
b = [1,2,43]

print(a is b,a==b)

a = 3
b = 3
print(a is b , a==b)