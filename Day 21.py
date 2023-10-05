def average(a,b):
    print("the average is: ",(a+b)/2)

def name1(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name1("Amy")

def name2(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name2(mname = "Peter", lname = "Wesker", fname = "Jade")

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill")

def name3(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name3("Peter", "Ego", "Quill")

def average2(*num):
    sum = 0
    for i in num:
        sum += i
    print(f"the average is {sum/len(num)}")
average2(1,2,3,4,5,6,7,8,9,3,3,45,1,1,3,432,5,235,2,354,4,13)

def name4(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name4(mname = "Buchanan", lname = "Barnes", fname = "James")

def name5(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name5("James", "Buchanan", "Barnes"))