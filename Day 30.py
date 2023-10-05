
# * factorial(7) = 7*6*5*4*3*2*1 = 5040
# * factorial(6) = 6*5*4*3*2*1 = 720 
# * factorial(5) = 5*4*3*2*1 = 120
# * factorial(4) = 4*3*2*1 = 24
# * factorial(3) = 3*2*1 = 6
# * factorial(2) = 2*1 = 2
# * factorial(1) = 1 = 1
# * factorial(0) = 1 = 1

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))
print(factorial(6))
print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))
print(factorial(0))



# ******************* Fibonacci Sequence ************************* #
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n - 1) + f(n+2)