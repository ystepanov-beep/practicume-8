text = str(input())
turn = 0
cities = text.lower().split()
for i in range(1, len(cities)):
    turn += 1
    if cities[i][0] == cities[i-1][-1]:
        pass
    else:
        turn -= 1
        break
if turn % 2 == 0:
    print('Петя выиграл')
else:
    print('Вася выиграл')
print(turn)