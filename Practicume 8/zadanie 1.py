text = str(input())
counter = 0
summ = 0
for i in range(len(text)):
    if text[i] == ' ':
        counter += 1
        summ = max(summ, counter)
    else:
        counter = 0
print(summ)
