country = ("Spain", "Italy", "India", "England", "Germany") 
print(country)
print(country[0])
print(country[1])
print(country[2])
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes