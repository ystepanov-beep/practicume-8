text = str(input())
for k in range(len(text.split()) - 1, -1, -1):
    print(text.split()[k], end = ' ')