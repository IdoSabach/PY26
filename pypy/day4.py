import random
computer_choice = ['Rock','Paper','Scissors']
player_choice = ['Rock','Paper','Scissors']
computer = 0
player = 0

while (computer < 5) and (player < 5):
    computer_c = random.choices(computer_choice)
    print(computer_c )
    player_c = int(input('0 for Rock, 1 for Paper and 2 for Scissors..'))
    print(player_c)

    if computer_c[0] == 'Rock':
        if player_c == 1:
            print(f'computer: {computer_c[0]}, player: {player_choice[player_c]}, point to player! ')
            player += 1
        elif player_c == 2:
            print(f'computer: {computer_c[0]}, player: {player_choice[player_c]}, point to computer! ')
            computer += 1
        else:
            continue
    elif computer_c[0] == 'Paper':
        if player_c == 2:
            print(f'computer: {computer_c[0]}, player: {player_choice[player_c]}, point to player! ')
            player += 1
        elif player_c == 0:
            print(f'computer: {computer_c[0]}, player: {player_choice[player_c]}, point to computer! ')
            computer += 1
        else:
            continue
    elif computer_c[0] == 'Scissors':
        if player_c == 0:
            print(f'computer: {computer_c[0]}, player: {player_choice[player_c]}, point to player! ')
            player += 1
        elif player_c == 1:
            print(f'computer: {computer_c[0]}, player: {player_choice[player_c]}, point to computer! ')
            computer += 1
        else:
            continue

    print(f'{computer}:{player}')

