# a = 9
# b = 8
# gmean = (a*b)/(a+b)
# print(gmean)
# c = 10
# d = 6
# gmean2 = (a*b)/(a+b)
# print(gmean2)

def calculateGmean(a,b):
    print((a*b)/(a+b))

def givesGreatorOne(a,b):
    if a>b:
        print(f"{a} is greator than {b}")
    elif a==b:
        pass
    else:
        print(f"{b} is greator than {a}")

def givesLesserOne(a,b):
    if a>b:
        print(f"{b} is smaller than {a}")
    elif a==b:
        pass
    else:
        print(f"{a} is smaller than {b}")

calculateGmean(2,3)
calculateGmean(1,4)
calculateGmean(8,34)
givesGreatorOne(1,2)
givesGreatorOne(64,56)
givesGreatorOne(642312421,53423126)
givesGreatorOne(642312,523126)
givesGreatorOne(5,5)
givesLesserOne(123,123)
givesLesserOne(12321,12213)
givesLesserOne(12321,122)
givesLesserOne(21,122)
givesLesserOne(5,5)