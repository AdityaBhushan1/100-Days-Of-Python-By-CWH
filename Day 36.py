try:
    num = int(input("Enter an integer: "))
# except Exception as e:
#     print(e)
except ValueError:
    print("Number entered is not an integer.")

print(num)