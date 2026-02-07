import sys
print('welcome to my game!')
go_to = input('you want left or right?')

if go_to == 'left':
    print(hex(id(go_to)))
    do_to = input('you want swim or walk?')
    if do_to == 'walk':
        print(hex(id(go_to)))
        color = input('blue, red or green?')
        if color == 'green':
            print(hex(id(go_to)))
            print('you win!!')
        else:
            print('game over!')
    else:
        print('game over!')
else:
    print('game over!')

print(hex(id(go_to)))
# print(sys.getrefcount(go_to), sys.getrefcount(do_to),sys.getrefcount(color))
print(sys.getrefcount(go_to))
print()
