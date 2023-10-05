# a = int(input("Enter any value between 5 and 9: "))
# if a<5 or a>9:
#     raise ValueError("Value should be between 5 and 9")

b = str(input("please enter 'quit': "))
if b.lower() == "quit":
    print("OK")
else:
    raise ValueError("Please Enter 'quit")