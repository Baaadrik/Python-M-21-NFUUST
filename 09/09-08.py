#~/college/python-nfbgu/09/
check = ["щи", "борщ", "щавельный суп", "овсяный суп", "суп по-чабански"]
i = int(input())
a = 0
while i != 0:
    print(check[i])
    a += 1
    if a == len(check) and i-1 != 0:
        a = 0
    i -= 1
