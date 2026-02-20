import keyword as key
def turn(name):
    if key.iskeyword(name):
        return False
    return name.isidentifier()
name = str(input())
if turn(name):
    print(f'{name} - допустимое имя в Python')
else:
    print(f'{name} - недопустимое имя в Python')