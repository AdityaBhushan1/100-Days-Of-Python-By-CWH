info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

print(info['name'])
print(info.get('eligible'))
print(info.values())
print(info.keys())
print(info.items())

for key in info.keys():
    print(f"the value of {key} is: {info[key]}")