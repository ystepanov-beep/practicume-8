print('Ведущий вводит строку: четырехзначное число с неповторяющимеся цифрами.')
num = str(input())
print('\n' * 25)
turn = 0
guess = str(input())
while True:
    turn += 1
    cows = 0
    bulls = 0
    for i in range(0, 4):
        if guess[i] in num:
            if guess[i] == num[i]:
                bulls += 1
            else:
                cows += 1
    print(f'Быков: {bulls} Коров: {cows}')
    if bulls == 4:
        print('Победа!')
        break
    if turn == 10:
        print('Проигрыш!')
        break
    guess = str(input())