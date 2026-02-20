text = str(input())
counter = 1
summ = 1
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        counter += 1
        summ = max(counter, summ)
    else:
        counter = 1
print(summ)
