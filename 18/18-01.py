
def matrix(stroka=1, stolb=0, num=0):
    if stroka == 1 and not stolb:
        stolb = 1
    elif stroka != 1 and not stolb:
        stolb = stroka
    return [[num for _ in range(stroka)] for _ in range(stolb)]

rows = matrix(2, 4, 3)
for row in rows:
    print(*row)