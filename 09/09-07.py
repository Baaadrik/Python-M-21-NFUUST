#~/college/python-nfbgu/09/
a = int(input())
check = list()

for i in range(a):
    check.append(input())

b = int(input())
search = list()
res = check.copy()

for n in range(b):
    check = res.copy()
    b = len(check)
    search.append(input())
    for r in range(a):
        if search[n] not in check[r]:
            res.remove(check[r])

for i in range(len(res)):
    print(res[i])
