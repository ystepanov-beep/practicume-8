text = str(input())
print(sorted([x for x in text.split()], key = len))