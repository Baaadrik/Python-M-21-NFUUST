#~/college/python-nfbgu/09/

num = int(input())
if num > 0:
    check = list()

    for i in range(n):
        check.append(input())

    words = int(input())
    if words > 0:
        for i in range(len(check)):
            print(check[i][words - 1], end='')
