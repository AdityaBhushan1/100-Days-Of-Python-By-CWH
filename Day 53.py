# cube = lambda x: x*x*x

# print(cube(2))

l = [1,2,3,4,6,4,3]

# newl = []
# for i in l:
#     newl.append(cube(i))

# * Easy Way to do a Thing Up there is Down There

# newl = list(map(cube, l))
# print(newl)

# ***********************************************#

# print(
#     list(
#         filter(
#             lambda a: a>4,l
#             )
#         )
#     )

# ************** #

from functools import reduce

num = [1,2,3,4,5]

sum = reduce(lambda x,y:x+y,num)
print(sum)


