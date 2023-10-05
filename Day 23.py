# l = [1,2,3,4,5]
# print(l)
# l.append(7)
# print(l)


# l = [23,534,123,1,46,75,1,1,2]
# l.sort()
# print(l)
# l.sort(reverse = True)
# print(l)
# l.reverse()
# print(l)
# print(l.index(1))
# print(l.count(1))

# colors = ["voilet", "green", "indigo", "blue"]
# newlist = colors.copy()
# print(colors)
# print(newlist)

# colors = ["voilet", "indigo", "blue"]
# colors.append("green")
# print(colors)


# colors = ["voilet", "indigo", "blue"]
# #           [0]        [1]      [2]

# colors.insert(1, "green")   #inserts item at index 1
# # updated list: colors = ["voilet", "green", "indigo", "blue"]
# #       indexs              [0]       [1]       [2]      [3]

# print(colors)

#add a list to a list
# colors = ["voilet", "indigo", "blue"]
# rainbow = ["green", "yellow", "orange", "red"]
# colors.extend(rainbow)
# print(colors)

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)