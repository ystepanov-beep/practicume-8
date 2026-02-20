stroke1 = str(input())
stroke2 = str(input())
stroke3 = str(input())
summ = []
for i in stroke1 + stroke2 + stroke3:
    if stroke1.count(i) > 0 and (stroke2 + stroke3).count(i) == 0:
        summ.append(i)
    elif stroke2.count(i) > 0 and (stroke3 + stroke1).count(i) == 0:
        summ.append(i)
    elif (stroke1 + stroke2).count(i) == 0 and stroke3.count(i) > 0:
        summ.append(i)
print(set(summ))