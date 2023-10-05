def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning!")
        fx(*args, **kwargs)
        print("thanks for using function")
    return mfx

@greet
def add(a,b):
    print(a+b)

greet(add)(1,2)
add(1,2)