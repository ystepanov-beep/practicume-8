def happy_ticket(number):
    if sum(int(x) for x in number[:len(number) // 2]) == sum(int(x) for x in number[len(number) // 2:]):
        return True
    return False
order = 0
while True:
    order += 1
    num = str(input('Номер билета: '))
    if len(num) % 2 == 0:
        if happy_ticket(num):
            print(order)
            break