students = {'name':'ido', 'age':25, 'courses': ['Java', 'Math']}
print(students)
print(students['name'])
print(students.get('name1', 'Not Found'))
print(students.get('phone', 'Not Found'))


print(hex(id(students)))

students['phone'] = '555-5555'
print(students)
print(hex(id(students)))

print(hex(id(students['name'])))
print(hex(id('phone')))


students.update({'name':'ido-sabah'})

print(students)
print(hex(id(students)))

print(hex(id(students['name'])))
print(hex(id('phone')))

print(len(students))
print(students.keys())
print(students.values())
print(students.items())

for key in students:
    print(key)

for key, value in students.items():
    print(key, value)

students.pop('phone')
print(students)


dict1 = {'name':'ido', 'age':25} 
dict2 = dict1.copy()
print(dict1)
print(dict2)
print(hex(id(dict1)))
print(hex(id(dict2)))
dict1.update({'phone': '555-55555'})

print(dict1)
print(dict2)
print(hex(id(dict1)))
print(hex(id(dict2)))

