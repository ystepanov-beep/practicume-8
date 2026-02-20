import keyword as k
def turn(name):
    if k.iskeyword(name):
        return False
    return name.isidentifier()
name = str(input())
if turn(name):
    print(f'{name} - допустимое имя в Python')
else:
    print(f'{name} - недопустимое имя в Python')