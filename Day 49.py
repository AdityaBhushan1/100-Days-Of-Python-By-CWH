# file io

# f = open('Day 49.txt','r')

# text = f.read()
# print(text)
# f.close()


# f = open('Day 49.txt','a')

# f.write("Hello World")
# f.close()

# f.write("Hello World")
# f.close()


with open('Day 49.txt', "a") as f:
    f.write("Hello World")