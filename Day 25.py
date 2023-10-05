# countries = ("Spain", "Italy", "India", "England", "Germany")
# print(countries)
# temp = list(countries)
# print(temp)
# temp.append("Russia")       #add item 
# print(temp)
# temp.pop(3)                 #remove item
# print(temp)
# temp[2] = "Finland"         #change item
# print(temp)
# countries = tuple(temp)
# print(countries)

# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)


Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)