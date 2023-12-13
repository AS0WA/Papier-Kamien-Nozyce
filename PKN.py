import random


symbols = ['p', 'k', 'n']
round_count = 0
player_points = 0
computer_points = 0

while True:
    round_count += 1
    while True:
        print(f"Runda numer: {round_count}")
        player_symbol = input('Podaj znak: papier(p), kamień(k), nożyce(n): \n')
        if player_symbol != 'p' and player_symbol != 'k' and player_symbol != 'n':
            print('Nie poprawna litera')
        else:
            break

    computer_symbol = random.choice(symbols)

    print(computer_symbol)

    if player_symbol == 'p':
        if computer_symbol == 'k':
            print('wygrywasz')
            player_points += 1
        elif computer_symbol == 'n':
            print('przegrywasz')
            computer_points += 1
        else:
            print('remis')
    elif player_symbol == 'k':
        if computer_symbol == 'n':
            print('wygrywasz')
            player_points += 1
        elif computer_symbol == 'p':
            print('przegrywasz')
            computer_points += 1
        else:
            print('remis')
    else:
        if computer_symbol == 'p':
            print('wygrywasz')
            player_points += 1
        elif computer_symbol == 'k':
            print('przegrywasz')
            computer_points += 1
        else:
            print('remis')

    print(f'Twoje punkty: {str(player_points)}')
    print(f'Punkty komputera: {str(computer_points)}\n')
