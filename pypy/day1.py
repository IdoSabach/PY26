import sys
name = input('What your name?\n')
band = input('What your favorite band?\n')
print('your name of band is ' + name + ' ' + band + '!' )

print(hex(id(name)))
size = sys.getsizeof(hex(id(name)))
print(size)

