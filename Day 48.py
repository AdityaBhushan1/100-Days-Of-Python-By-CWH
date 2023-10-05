x = 10 # global variable

def my_func():
    global x
    x = 4
    y = 5 # local variable
    print(y)

my_func()
print(x)

# print(y) # this will give an error
