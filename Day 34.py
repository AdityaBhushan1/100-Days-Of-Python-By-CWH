info = {'name':'Karan', 'age':19, 'eligible':True}


print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

info.pop('eligible')
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# del info
# print(info)

info.clear()
print(info)