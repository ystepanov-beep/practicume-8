text = str(input())
summ = []
for i in text:
    summ.append(i)
if text.count(' ') > 0:
    print(len(set(summ)) - 1)
else:
    print(len(set(summ)))