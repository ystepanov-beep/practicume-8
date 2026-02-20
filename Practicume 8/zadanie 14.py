print('Ведущий вводит две строки: подсказку и загаданное слово.')
tooltip = str(input())
word = str(input())
print('\n' * 25)
turn = 0
guess = '*' * len(word)
while True:
    turn += 1
    print(tooltip)
    print(guess)
    switch = int(input('Буква или слово (0 - буква, 1 - слово)?0'))
    if switch == 0:
        letter = str(input())
        if word.count(letter) > 0:
            for i in range(len(word)):
                if word[i] == letter:
                    guess = guess[:i] + letter + guess[i+1:]
    else:
        wordguess = str(input())
        if wordguess == word:
            print('Победа!')
            break
        else:
            print('Проигрыш!')
    if turn == 10:
        print('Проигрыш!')
        break