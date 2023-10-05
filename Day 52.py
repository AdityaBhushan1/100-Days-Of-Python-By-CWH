# def double(x):
#     return x*2

def appl(fx,value):
    return 6 + fx(value)

double = lambda x:x*2
cube = lambda x: x*x*x
average = lambda x,y: (x+y)/2


print(double(2))
print(cube(2))
print(average(2,3))

print(appl(cube,2))