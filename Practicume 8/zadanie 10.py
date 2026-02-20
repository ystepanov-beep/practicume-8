text = str(input())
def unique(word):
    for i in word:
        if word.count(i) == 1:
            pass
        else:
            return False
    return True
for i in text.split():
    if i != text.split()[0] and unique(i):
        print(i, end = ' ')