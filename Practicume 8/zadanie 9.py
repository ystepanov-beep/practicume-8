text = str(input())
for i in text.split():
    if text.count(i) == 2:
        print(i)
        break
